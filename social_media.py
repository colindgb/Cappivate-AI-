import tweepy

API_KEY = "your_twitter_api_key"
API_SECRET = "your_twitter_api_secret"
ACCESS_TOKEN = "your_twitter_access_token"
ACCESS_SECRET = "your_twitter_access_secret"

def post_to_twitter(content):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(content)
    print("Posted successfully!")
