import requests, json, config
from requests_oauthlib import OAuth1

url = 'https://stream.twitter.com/1.1/statuses/sample.json'
auth = OAuth1(config.consumerKey, config.consumerSecret, config.accessToken, config.accessSecret)
file = open('tweets.txt', 'w')
r = requests.get(url, auth=auth, stream=True)

for line in r.iter_lines():
    if line:
        decoded_line = line.decode('utf-8')
        text = json.loads(decoded_line)
        print(text)
        file.write(text + '\n')
