CREATE TABLE IF NOT EXISTS comments (
    id TEXT PRIMARY KEY,
    post_id TEXT,
    subreddit TEXT,
    author TEXT,
    body TEXT,
    created_utc REAL,
    score INTEGER,
    sentiment TEXT,
    emotion TEXT
);