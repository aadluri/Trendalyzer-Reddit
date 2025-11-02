import os
from dotenv import load_dotenv

load_dotenv()

# API creds, make a note to set these in .env file
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT", "reddit_trend_analyzer")

# Database path - need to run scripts to create this
DB_PATH = os.getenv("DB_PATH", "db/reddit_trends.db")

# Subreddit list
SUBREDDITS = ["HomeDecorating", "InteriorDesign", "DesignMyRoom", "CozyPlaces", "interiordecorating"]

# too many posts may lead to rate , i would like 30-40
POST_LIMIT = 10