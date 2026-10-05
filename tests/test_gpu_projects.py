import unittest
from starlette.testclient import TestClient
from main import app


class GPUProjectTests(unittest.TestCase):
    def setUp(self):
        self.client=TestClient(app)
        self.addCleanup(self.client.close)

    def test_projects_navigation_and_recorded_results(self):
        for path in ('/','/projects','/sitemap.xml'):
            text=self.client.get(path).text
            for slug in ('ml-compiler-lab','tile-accelerator'):
                self.assertIn('/projects/'+slug,text)
        page=self.client.get('/projects/ml-compiler-lab')
        self.assertEqual(page.status_code,200)
        self.assertIn('GPU kernels and model compilation',page.text)
        self.assertIn('https://github.com/russedavid/ml-compiler-lab',page.text)
        self.assertNotIn('Related hardware runtime work',page.text)
        self.assertNotIn('tinygrad/tinygrad/pull/17369',page.text)
        self.assertIn('Global-memory intermediate',page.text)
        self.assertIn('1,000 observations',page.text)
        fragment=self.client.get('/projects/ml-compiler-lab/results/1',headers={'HX-Request':'true'})
        self.assertEqual(fragment.status_code,200)
        self.assertIn('Rows 49, channels 48, hidden width 96',fragment.text)
        self.assertNotIn('<html',fragment.text)
        self.assertEqual(self.client.get('/projects/ml-compiler-lab/results/99').status_code,404)
        self.assertEqual(self.client.get('/projects/ml-compiler-lab?case=bad').status_code,200)

    def test_simulator_page_and_bundled_assets(self):
        page=self.client.get('/projects/tile-accelerator')
        self.assertEqual(page.status_code,200)
        self.assertIn('compiler and simulator for tiled',page.text)
        self.assertIn('analytical estimates',page.text)
        for path in ('/public/data/gpu-kernel-results.json','/public/data/tile-accelerator-results.json',
                     '/public/images/gpu-kernel-assessment.svg','/public/images/tile-architecture-study.svg'):
            self.assertEqual(self.client.get(path).status_code,200,path)
        self.assertEqual(self.client.get('/public/sun.png').status_code,200)
