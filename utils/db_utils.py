import sqlite3

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id TEXT PRIMARY KEY,
            title TEXT,
            score INTEGER,
            url TEXT,
            created_utc REAL,
            subreddit TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id TEXT PRIMARY KEY,
            post_id TEXT,
            body TEXT,
            sentiment TEXT,
            created_utc REAL,
            FOREIGN KEY(post_id) REFERENCES posts(id)
        )
    ''')
    conn.commit()
    conn.close()

def insert_post(db_path, post):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(
        "INSERT OR IGNORE INTO posts VALUES (?, ?, ?, ?, ?, ?)",
        (post.id, post.title, post.score, post.url, post.created_utc, post.subreddit.display_name)
    )
    conn.commit()
    conn.close()

def insert_comment(db_path, comment_id, post_id, body, sentiment, created_utc):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(
        "INSERT OR IGNORE INTO comments VALUES (?, ?, ?, ?, ?)",
        (comment_id, post_id, body, sentiment, created_utc)
    )
    conn.commit()
    conn.close()
