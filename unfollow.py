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

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

start = time.time()
i = 0
friends=api.friends_ids(SCREEN_NAME)

print("You have", len(friends), "friends.")
while(1):
    proceed=input("Proceeding will unfollow all accounts. Are you sure you'd like to proceed [Y/N]: ")
    if proceed.lower() == "y" or proceed.lower() == "yes":
        for u in friends:
            print("Unfollowing", api.get_user(u).screen_name)
#           api.destroy_friendship(u)
            i = i + 1
        if i == 1:
            print(i, "friend unfollowed")
            print ()
        else:
            print(i, "friends unfollowed")
            print()
        break

    elif proceed.lower() == "n" or proceed.lower() == "no":
        print("Stopping Unfollow")
        break
    else:
        print("Invalid Selection. Try again.")
