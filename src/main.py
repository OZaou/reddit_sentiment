
import yaml
from sentiment_analyzer import BERTSentimentAnalyzer
from reddit_parser import fetch_reddit_posts
from visualization import plot_sentiment
from collections import defaultdict
import logging

def analyze_and_plot_sentiment(config):
    analyzer = BERTSentimentAnalyzer()
    sentiment_counts = defaultdict(lambda: defaultdict(int))

    for subreddit in config['reddit']['subreddit_list']:
        posts = fetch_reddit_posts(config['reddit']['ticker'], config['reddit']['post_limit'], subreddit)
        
        for post in posts:
            text = post 
            sentiment = analyzer.analyze(text)
            sentiment_counts[subreddit][sentiment] += 1
 
    plot_sentiment(sentiment_counts)

if __name__ == "__main__":
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    logging.basicConfig(level=logging.INFO)
    
    analyze_and_plot_sentiment(config)