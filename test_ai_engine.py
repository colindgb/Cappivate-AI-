import unittest
from backend.ai_engine import generate_content
class TestAIEngine(unittest.TestCase):
    def test_content(self):
        self.assertTrue(len(generate_content('Test')) > 0)
