# visualization.py

import matplotlib.pyplot as plt

def plot_sentiment(sentiment_data):
    subreddits = list(sentiment_data.keys())
    sentiments = {'positive': [], 'neutral': [], 'negative': []}

    for subreddit, sentiment_count in sentiment_data.items():
        sentiments['positive'].append(sentiment_count.get('positive', 0))
        sentiments['neutral'].append(sentiment_count.get('neutral', 0))
        sentiments['negative'].append(sentiment_count.get('negative', 0))

    x = range(len(subreddits))

    plt.bar(x, sentiments['positive'], color='green', label='Positive')
    plt.bar(x, sentiments['neutral'], bottom=sentiments['positive'], color='gray', label='Neutral')
    plt.bar(x, sentiments['negative'], bottom=[sum(val) for val in zip(sentiments['positive'], sentiments['neutral'])], color='red', label='Negative')

    plt.xticks(x, subreddits, rotation=90)
    plt.xlabel("Subreddits")
    plt.ylabel("Sentiment Count")
    plt.title("Sentiment Analysis Across Subreddits")
    plt.legend()
    plt.tight_layout()
    plt.show()
