from ntscraper import Nitter

def main():
    scraper = Nitter(log_level=1, skip_instance_check=False)
    keywords = ["devin booker", "kevin durant"]
    scrape = scraper.get_tweets(keywords, mode='term',number=1)
    print(scrape)
    print("----------------------------")
    only_text = [tweet['text'] for tweet in scrape['tweets']]
    print(only_text)

if __name__ == "__main__":
    main()


