from ntscraper import Nitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(tweets):
    """Process tweets and determine overall sentiment."""
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = [analyzer.polarity_scores(tweet)['compound'] for tweet in tweets]

    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0

    if avg_sentiment > 0.05:
        sentiment_label = "Mostly Positive"
    elif avg_sentiment < -0.05:
        sentiment_label = "Mostly Negative"
    else:
        sentiment_label = "Neutral"

    return sentiment_label, avg_sentiment, sentiment_scores

def format_newsletter(keyword, sentiment_label, avg_sentiment, tweets, sentiment_scores):
    """Format sentiment summary for newsletter."""
    num_positive = sum(1 for s in sentiment_scores if s > 0.05)
    num_negative = sum(1 for s in sentiment_scores if s < -0.05)
    num_neutral = len(sentiment_scores) - (num_positive + num_negative)

    example_tweet = tweets[0] if tweets else "No tweets found."

    return f"""
    🔵 **{keyword.title()}**  
    - **Overall Sentiment:** {sentiment_label} (Avg Score: {avg_sentiment:.2f})  
    - **Example Tweet:** "{example_tweet}"  
    - **Sentiment Breakdown:**  
      - 📉 Negative: {num_negative} tweets  
      - 😐 Neutral: {num_neutral} tweets  
      - 📈 Positive: {num_positive} tweets  
    """

def main():
    scraper = Nitter(log_level=1, skip_instance_check=False)
    user_keywords = ["donald trump"]  # Example keywords
    newsletter_content = "📰 **Daily Sentiment Report**\n"

    for keyword in user_keywords:
        scrape = scraper.get_tweets(keyword, mode='term', number=5)
        only_text = [tweet['text'] for tweet in scrape['tweets']]

        sentiment_label, avg_sentiment, sentiment_scores = analyze_sentiment(only_text)
        summary = format_newsletter(keyword, sentiment_label, avg_sentiment, only_text, sentiment_scores)
        newsletter_content += summary + "\n"

    print(newsletter_content)  # Replace with email or app notification logic

if __name__ == "__main__":
    main()
