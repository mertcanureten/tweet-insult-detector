import tweepy
import os
from dotenv import load_dotenv

# .env
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

# API'ye bağlan
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Mentionları çek
def get_mentions():
    mentions = api.mentions_timeline(tweet_mode='extended', count=100)  # En son 100 tweet
    tweet_data = []
    for mention in mentions:
        tweet_data.append({
            'text': mention.full_text,
            'user': mention.user.screen_name,
            'date': mention.created_at
        })
    return tweet_data
