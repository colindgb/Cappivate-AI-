import unittest
import requests

BASE_URL = "http://127.0.0.1:8000"  # Change this if deployed on a server

class TestCappivateAI(unittest.TestCase):
    
    def test_api_connection(self):
        """Check if the API server is running."""
        response = requests.get(BASE_URL + "/")
        self.assertEqual(response.status_code, 200)
        print("✅ API Server is running correctly")

    def test_ai_content_generation(self):
        """Test AI-powered content generation."""
        payload = {"prompt": "Launching a new product", "style": "engaging"}
        response = requests.post(BASE_URL + "/generate_content", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("content" in response.json())
        print("✅ AI Content Generation Passed")

    def test_social_media_posting(self):
        """Test automated social media posting (simulated)."""
        payload = {"platform": "twitter", "content": "This is a test post"}
        response = requests.post(BASE_URL + "/post_content", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("status"), "posted")
        print("✅ Social Media Auto-Posting Passed")

    def test_trend_analysis(self):
        """Test AI-driven trend monitoring."""
        response = requests.get(BASE_URL + "/trending_hashtags?platform=twitter")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("hashtags" in response.json())
        print("✅ AI Trend Analysis Passed")

    def test_auto_commenting(self):
        """Test AI-powered auto-replies to comments."""
        payload = {"comment": "This is amazing!"}
        response = requests.post(BASE_URL + "/auto_reply", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("response" in response.json())
        print("✅ AI Auto-Commenting Passed")

if __name__ == "__main__":
    unittest.main()
