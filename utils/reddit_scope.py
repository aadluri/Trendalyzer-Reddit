'''Fetch and print Reddit API scopes and their descriptions. straight from Reddit oAuth docs:
https://praw.readthedocs.io/en/stable/tutorials/refresh_token.html#refresh-token'''
import requests

response = requests.get(
    "https://www.reddit.com/api/v1/scopes.json",
    headers={"User-Agent": "fetch-scopes by u/bboe"},
)

for scope, data in sorted(response.json().items()):
    print(f"{scope:>18s}  {data['description']}")
