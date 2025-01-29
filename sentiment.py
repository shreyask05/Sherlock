from ntscraper import Nitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def main():
    scraper = Nitter(log_level=1, skip_instance_check=False)
    keywords = ["donald trump"]
    scrape = scraper.get_tweets(keywords, mode='term',number=5)
    analyzer = SentimentIntensityAnalyzer()
    only_text = [tweet['text'] for tweet in scrape['tweets']]
    for tweet in only_text:
        sentiment = analyzer.polarity_scores(tweet)
        print(f"Tweet: {tweet}")
        print(f"Sentiment Scores: {sentiment}\n")

if __name__ == "__main__":
    main()


