import requests

def get_trending_hashtags(platform="twitter"):
    if platform == "twitter":
        url = "https://api.twitter.com/2/tweets/search/recent?query=trending"
        headers = {"Authorization": f"Bearer YOUR_TWITTER_API_TOKEN"}
        response = requests.get(url, headers=headers)
        return response.json()
    return []
