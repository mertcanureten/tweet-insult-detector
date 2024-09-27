import pandas as pd

def save_report(insult_tweets):
    df = pd.DataFrame(insult_tweets, columns=['tweet', 'user', 'date'])
    df.to_csv('insult_report.csv', index=False)
    print("Rapor kaydedildi.")
