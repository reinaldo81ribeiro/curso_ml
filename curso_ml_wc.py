
import tweepy
import time
import csv

cons_key = "7hsppVq26xRNndnGg2tPhMObQ"
cons_secret = "rtlfgDxQCCI4VJ72sZQalryNhnnSMZcUzflX9F3xIjWn6PgGS5"
tok_key = "FFTKLYY7K33DVFEWd8Xg6N9hadhnST2"
tok_secret = "OfPtsrrDJ7U4JLPejn6i0VCIAYfcOXHDNG431WP9U9lkK"

auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(tok_key, tok_secret)

api = tweepy.API(auth)

arq = csv.writer(open("base_teste.csv", "w"))
arq2 = open("base_teste.json", "w")

row = []

statuses = tweepy.Cursor(api.search, q="#brazil", sin="2017-08-27", until="2017-08-28", lang="en").items()

while True:
    try:
        status = statuses.next()
        print(status)
        exit()
    except tweepy.TweepError:
        print("agurde 15 minutos")    
        time.sleep(60*15)
        continue
    except StopIteration:
        break
