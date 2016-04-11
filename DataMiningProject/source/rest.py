import csv

import tweepy

import Conf

count=0
q = '#gopdebate'
auth = tweepy.OAuthHandler(Conf.consumer_key, Conf.consumer_secret)
auth.set_access_token(Conf.access_token, Conf.access_secret)
tweet_data = []
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search,q,since='2016-04-08',until='2016-04-09').items(180):
    tweet_data.append(tweet.text.encode('utf-8'))

with open("data/raw_tweets4.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in tweet_data:
        writer.writerow([val])
exit()

