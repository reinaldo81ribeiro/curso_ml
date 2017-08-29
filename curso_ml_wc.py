#   coding: utf-8

import tweepy
import time
import csv

cons_key = "TMOWMdgN7U2LuygzQonoJHsrc"
cons_secret = "m65XdfcY0w5cXqCdVg3aG9dX7mWJh79aW2NpdQkfn9v4mgkpxH"
tok_key = "FFTKLYY7K33DVFEWd8Xg6N9hadhnST2"
tok_secret = "OfPtsrrDJ7U4JLPejn6i0VCIAYfcOXHDNG431WP9U9lkK"

auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(tok_key, tok_secret)

api = tweepy.API(auth)
print(api.proxy)


arq = csv.writer(open("base_teste.csv", "w"))
arq2 = open("base_teste.json", "w")

row = []

statuses = tweepy.Cursor(api.search, q="#brazil", sin="2017-08-27", until="2017-08-28", lang="en").items()

while True:
    try:
        for status in statuses:
            print(status)
            exit()

        exit()
    except tweepy.TweepError:
        print("agurde 15 minutos")    
        time.sleep(60*15)
        continue
    except StopIteration:
        break
