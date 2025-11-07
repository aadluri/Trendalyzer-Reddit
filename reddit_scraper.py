import praw
from src.config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, USER_AGENT, DB_PATH
from utils.db_utils import init_db, insert_post, insert_comment
from src.text_sentiment import analyze_sentiment

def get_reddit_instance():
    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=USER_AGENT
    )

def scrape_subreddit(subreddit_name="HomeDecorating", limit=50):
    reddit = get_reddit_instance()
    init_db(DB_PATH)
    subreddit = reddit.subreddit(subreddit_name)

    for submission in subreddit.hot(limit=limit):
        insert_post(DB_PATH, submission)
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            sentiment = analyze_sentiment(comment.body)
            insert_comment(DB_PATH, comment.id, submission.id, comment.body, sentiment, comment.created_utc)

if __name__ == "__main__":
    scrape_subreddit("HomeDecorating", limit=20)
