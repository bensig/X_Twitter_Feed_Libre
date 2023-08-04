import csv
import json
import re
import sys

filename = "index.json"


def extract_tweet_id(url):
    # Extract tweet ID from the URL using regular expression
    return re.search(r"/status/(\d+)", url).group(1)


def csv_to_json(input_file):
    # Read data from CSV file and create a dictionary with token as key and tweet IDs as values
    data = {}
    with open(input_file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                token, url = row
                tweet_id = extract_tweet_id(url)
                data.setdefault(token, []).append(tweet_id)

    # Convert the dictionary to JSON
    json_data = json.dumps(data, indent=2)

    # Save the JSON data to "tweets.json"
    with open(filename, "w") as jsonfile:
        jsonfile.write(json_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py data.csv")
    else:
        input_file = sys.argv[1]
        csv_to_json(input_file)
