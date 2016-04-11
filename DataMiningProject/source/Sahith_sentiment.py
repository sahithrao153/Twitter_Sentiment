import csv
import time

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

import Conf
import json

start_time = time.time()

# setting up the keys

class TweetListener(StreamListener):
    # A listener handles tweets are the received from the stream.
    # This is a basic listener that just prints received tweets to standard output
    def __init__(self, start_time, time_limit=60, counter=0):
        self.count = counter
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []

    def display(self):
        print self.tweet_data


    def on_data(self, data):
        while self.count < 5:
            try:
                self.count += 1
                data_json = json.loads(data)
                data_text=data_json['text']
                self.tweet_data.append(data_text.encode('utf-8'))
                return True
            except BaseException, e:
                print 'failed ondata,', e.message
                pass
        with open("raw.csv", "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in self.tweet_data:
               writer.writerow([val])
        exit()

    def on_error(self, status):
        print status

# printing all the tweets to the standard output
auth = OAuthHandler(Conf.consumer_key, Conf.consumer_secret)
auth.set_access_token(Conf.access_token, Conf.access_secret)

stream = Stream(auth, TweetListener(start_time, time_limit=20, counter=0))
stream.filter(track=['gopdebate'])


