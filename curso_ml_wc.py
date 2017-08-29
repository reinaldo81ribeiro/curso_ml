
import tweepy
import time
import csv

cons_key = ""
cons_secret = ""
tok_key = ""
tok_secret = ""

auth = tweepy.OAuthHandler(cons_key, cons_secret)
#auth.set_access_token(tok_key, tok_secret)

api = tweepy.API(auth)

arq = csv.writer(open("base_teste.csv", "w"))
arq2 = open("base_teste.json", "w")

row = []

statuses = tweepy.Cursor(api.search, q="#brazil", sin="2017-08-27", until="2017-08-28", lang="en").items()

while True:
    try:
        status = statuses.next()
        print(80*"=")
        print(status)
        exit()
    except tweepy.TweepError:
        print("agurde 15 minutos")    
        time.sleep(60*15)
        continue
    except StopIteration:
        print("acabou")
        break
