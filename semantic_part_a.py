import twitter
import json

# Ερώτημα Α
keys = json.load(open('data/json/keys.json'))

consumer_key = keys['api_key']
consumer_secret = keys['api_secret']
access_token_key = keys['access_token']
access_token_secret = keys['access_secret']
api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                  access_token_key=access_token_key, access_token_secret=access_token_secret)

print(type(api.VerifyCredentials()))
# json.dump(api.VerifyCredentials().__dict__, open(
# 'data/json/credentials.json', 'w'), indent=4)
