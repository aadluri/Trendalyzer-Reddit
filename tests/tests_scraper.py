from src.reddit_scraper import get_reddit_instance

def test_reddit_auth():
    reddit = get_reddit_instance()
    assert reddit.user.me() is None  # Should connect anonymously
    assert reddit.read_only is True  # Should be in read-only mode