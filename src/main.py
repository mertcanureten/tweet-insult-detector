from twitter_api import get_mentions
from text_cleaning import clean_tweet
from insult_detection import detect_insult
from report_generation import save_report

def main():
    # Etiketlendiğin tweet'leri çek
    mentions = get_mentions()
    insult_tweets = []

    for mention in mentions:
        tweet = clean_tweet(mention['text'])
        if detect_insult(tweet):
            insult_tweets.append({
                'tweet': tweet,
                'user': mention['user'],
                'date': mention['date']
            })

    # Hakaret içerikli tweet'leri listele ve raporla
    save_report(insult_tweets)

if __name__ == "__main__":
    main()
