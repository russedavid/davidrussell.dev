"""Check the behavior promised by the authored retry-policy illustration."""
import unittest

from project_examples import RETRY_V1, RETRY_V2


def function_from_example(code):
    namespace = {}
    exec(compile(code, '<authored website example>', 'exec'), namespace)
    return namespace['retry_delay']


class RetryExampleTests(unittest.TestCase):
    def test_both_versions_keep_replay_safety_and_the_retry_budget(self):
        for code in (RETRY_V1, RETRY_V2):
            retry = function_from_example(code)
            for status in (429, 500, 503, 599):
                self.assertIsNone(retry(status, 1, safe_to_retry=False))
                self.assertIsNone(retry(status, 4, safe_to_retry=True))
            self.assertEqual([retry(503, n, safe_to_retry=True) for n in (1, 2, 3)], [1, 2, 4])
            for status in (200, 400, 499, 600):
                self.assertIsNone(retry(status, 1, safe_to_retry=True))

    def test_new_requirement_adds_rate_limiting_and_preserves_server_delays(self):
        first = function_from_example(RETRY_V1)
        revised = function_from_example(RETRY_V2)
        self.assertIsNone(first(429, 1, safe_to_retry=True))
        self.assertEqual(revised(429, 1, safe_to_retry=True), 1)
        for status in (429, 503):
            for seconds in (0, 7, 10):
                self.assertEqual(revised(status, 1, safe_to_retry=True, retry_after=seconds), seconds)
            # Do not clamp a longer server delay and retry earlier than requested.
            self.assertIsNone(revised(status, 1, safe_to_retry=True, retry_after=30))
            self.assertIsNone(revised(status, 1, safe_to_retry=True, retry_after=-1))
