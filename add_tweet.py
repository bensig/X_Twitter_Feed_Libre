import json
import sys
import re


def extract_tweet_id(url_or_id):
    # Check if the input is a URL and extract the tweet ID
    tweet_id_match = re.search(r"/status/(\d+)", url_or_id)
    if tweet_id_match:
        return tweet_id_match.group(1)
    else:
        return url_or_id


def add_tweet_to_json(token, tweet_id):
    # Load the existing JSON data from "index.json"
    try:
        with open("index.json", "r") as jsonfile:
            data = json.load(jsonfile)
    except FileNotFoundError:
        data = {}

    # Check if the token already exists in the JSON data
    if token in data:
        tweet_id = extract_tweet_id(tweet_id)
        # Check if the tweet ID already exists in the array
        if tweet_id not in data[token]:
            data[token].append(tweet_id)
        else:
            print("Duplicate tweet ID. Not adding to the array.")
    else:
        data[token] = [extract_tweet_id(tweet_id)]

    # Save the updated JSON data to "index.json"
    with open("index.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_tweet.py TOKEN TWEET_ID_OR_URL")
    else:
        token = sys.argv[1]
        tweet_id_or_url = sys.argv[2]
        add_tweet_to_json(token, tweet_id_or_url)
