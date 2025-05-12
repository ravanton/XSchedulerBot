import os
import requests

def post_tweet(text):
    token = os.getenv("TWITTER_BEARER_TOKEN")
    if not token:
        raise Exception("Twitter token not found in environment variables.")

    url = "https://api.twitter.com/2/tweets"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {"text": text}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 201:
        raise Exception(f"Failed to post tweet: {response.status_code} - {response.text}")
