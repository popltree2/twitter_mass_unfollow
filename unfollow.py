#! /usr/bin/python
import tweepy
import time
from keys import keys

SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

start = time.time()
i = 0
friends=api.friends_ids(SCREEN_NAME)

while (1):
    try:
        for u in friends:
            print ("Unfollowing", api.get_user(u).screen_name)
            api.destroy_friendship(u)
    except:
        print "Possibly rate limited. Waiting 60 seconds."
        time.sleep(60)
