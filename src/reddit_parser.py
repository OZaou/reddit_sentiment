import praw
import logging

def fetch_reddit_posts(ticker, limit=1000, subreddit_name="wallstreetbets"):
    try:
        reddit = praw.Reddit(
            client_id="UoX9YHbr5O2AulsL2VXCSQ",
            client_secret="HK4I2PXAEzqmViJVKOfkxCO-AdpEVA",
            user_agent="testredd"
        )
        subreddit = reddit.subreddit(subreddit_name)
        query = f"{ticker}"
        posts = [submission.title for submission in subreddit.search(query, limit=limit)]
        return posts
    except Exception as e:
        logging.error(f"Error fetching Reddit posts from r/{subreddit_name}: {e}")
        return []