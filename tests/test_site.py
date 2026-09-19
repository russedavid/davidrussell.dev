import unittest
from unittest.mock import Mock, patch

import requests
from starlette.testclient import TestClient

from air_quality import fetch_aqi_data
from main import app


class SiteTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.addCleanup(self.client.close)

    def test_existing_pages_and_public_assets(self):
        for path in ("/", "/about", "/tools", "/blog", "/blog/fury-road-redemption", "/public/sun.png"):
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 200)
        for path in ("/.sesskey", "/main.py", "/requirements.txt", "/public/%2e%2e/main.py"):
            self.assertEqual(self.client.get(path).status_code, 404)

    def test_career_project_navigation_and_fictional_walkthrough(self):
        response = self.client.get("/projects/career-workbench")
        self.assertEqual(response.status_code, 200)
        self.assertIn("A good resume starts before the writing", response.text)
        self.assertIn("https://github.com/russedavid/career-workbench", response.text)
        self.assertIn("authenticated Codex CLI", response.text)
        self.assertIn("Fixed, self-authored fictional example", response.text)
        for path in ("/", "/projects", "/sitemap.xml"):
            self.assertIn("/projects/career-workbench", self.client.get(path).text)
        fragment = self.client.get("/projects/career-workbench/walkthrough/1", headers={"HX-Request": "true"})
        self.assertIn("Dependent draft needs review", fragment.text)
        self.assertNotIn("<html", fragment.text)
        self.assertEqual(self.client.get("/projects/career-workbench/walkthrough/9").status_code, 404)
        self.assertIn("Shared contribution retained", self.client.get("/projects/career-workbench?step=2").text)
        self.assertIn("Source recorded", self.client.get("/projects/career-workbench?step=bad").text)

    def test_form_submission_missing_and_invalid_values_do_not_call_provider(self):
        with patch("air_quality.requests.post") as call:
            for values in ({}, {"api_key": "test-only", "coordinates": "nan,1\n91,2\nnot coordinates"}):
                response = self.client.post("/check-aqi", data=values, headers={"HX-Request": "true"})
                self.assertEqual(response.status_code, 200)
                self.assertIn('role="alert"', response.text)
                self.assertNotIn("<html", response.text)
            call.assert_not_called()

    def test_training_project_links_and_walkthrough_navigation(self):
        page = self.client.get("/projects/qwen-ttrpg")
        self.assertEqual(page.status_code, 200)
        self.assertIn("Training an AI to take its turn", page.text)
        self.assertIn("https://github.com/russedavid/qwen-ttrpg", page.text)
        self.assertIn("https://github.com/russedavid/format_conversation_dataset", page.text)
        self.assertIn("Fixed, self-authored fictional illustration", page.text)
        for path in ("/", "/projects", "/sitemap.xml"):
            self.assertIn("/projects/qwen-ttrpg", self.client.get(path).text)
        fragment = self.client.get("/projects/qwen-ttrpg/walkthrough/1", headers={"HX-Request": "true"})
        self.assertIn("Loss belongs to the response", fragment.text)
        self.assertNotIn("<html", fragment.text)
        self.assertIn("Check the weights, then the behavior", self.client.get("/projects/qwen-ttrpg?step=2").text)
        for value in ("bad", "-1", "99"):
            self.assertIn("A response needs its context", self.client.get(f"/projects/qwen-ttrpg?step={value}").text)
        self.assertEqual(self.client.get("/projects/qwen-ttrpg/walkthrough/99").status_code, 404)

    def test_aqi_results_keep_successful_locations_when_another_lookup_fails(self):
        valid = Mock()
        valid.json.return_value = {"hoursInfo": [{"indexes": [{"aqi": 0}]}]}
        failed = requests.RequestException("URL contained test-secret")
        with patch("air_quality.requests.post", side_effect=[valid, failed]):
            response = self.client.post("/check-aqi", data={"api_key": "test-secret", "coordinates": "30,-97\n40,-70"}, headers={"HX-Request": "true"})
        self.assertIn("Average AQI: 0.00", response.text)
        self.assertIn("could not complete", response.text)
        self.assertNotIn("test-secret", response.text)

    def test_empty_data_is_not_reported_as_zero_and_native_form_has_a_page(self):
        result = Mock()
        result.json.return_value = {"hoursInfo": []}
        with patch("air_quality.requests.post", return_value=result):
            response = self.client.post("/check-aqi", data={"api_key": "test-only", "coordinates": "30,-97"})
        self.assertIn("No air-quality readings", response.text)
        self.assertIn("<html", response.text)

    def test_pagination_is_followed_and_repeated_tokens_stop(self):
        first, second = Mock(), Mock()
        first.json.return_value = {"hoursInfo": [{"indexes": [{"aqi": 10}]}], "nextPageToken": "page2"}
        second.json.return_value = {"hoursInfo": [{"indexes": [{"aqi": 20}]}]}
        with patch("air_quality.requests.post", side_effect=[first, second]) as call:
            self.assertEqual(fetch_aqi_data("test-only", 30, -97)["average_aqi"], 15)
            self.assertEqual(call.call_args.kwargs["json"]["pageToken"], "page2")
        with patch("air_quality.requests.post", return_value=first), self.assertRaisesRegex(ValueError, "repeated"):
            fetch_aqi_data("test-only", 30, -97)


if __name__ == "__main__":
    unittest.main()
