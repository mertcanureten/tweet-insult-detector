import re

def clean_tweet(tweet):
    tweet = re.sub(r'http\S+', '', tweet)  # linkleri kaldır
    tweet = re.sub(r'@\w+', '', tweet)     # mention'ları kaldır
    tweet = re.sub(r'#\w+', '', tweet)     # hashtag'leri kaldır
    tweet = re.sub(r'[^\w\s]', '', tweet)  # noktalama işaretlerini kaldır
    return tweet.lower()
