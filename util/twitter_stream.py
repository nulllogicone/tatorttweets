#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

from twython import TwythonStreamer, Twython
from datetime import datetime, timedelta
import sqlite3 as lite
import os
import sys
import urllib3
import time
import generate_all

import warnings
warnings.filterwarnings("ignore")
urllib3.disable_warnings()

# sys.stdout = open('output' + str(datetime.now()) + '.txt' , 'w')
sys.stdout = open('output.txt' , 'w')


episodenumber = 0 
filename = os.path.join(os.path.dirname(__file__), '../tweets.db')
con = lite.connect(filename)

start = time.time()
now = datetime.now()
print 'now: ' + str(now) 
stoppingtime = now + timedelta(minutes=120)
print 'stoppingtime: ' + str(stoppingtime) 

import twitterconfig 
twitter = Twython(twitterconfig.APP_KEY, twitterconfig.APP_SECRET, twitterconfig.OAUTH_TOKEN, twitterconfig.OAUTH_TOKEN_SECRET)


    
class MyStreamer(TwythonStreamer):
    
    originalcounter = 0
    retweeted = 0
    retweets = {}

    
    def on_success(self, tweet):
        
        try: 
        
            
            sys.stdout.flush()
            
            
            if (datetime.now() > stoppingtime): 
                    print 'disconnect'
                    print 'time since start: ' + str(time.time() - start) + ' seconds'
                    self.disconnect()
    
    
         
            if 'text' in tweet:
                
                text = tweet['text']  
                tweettime = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
                tweettime += timedelta(hours=1) # winter time 
    #           tweettime += timedelta(hours=2)  # summer time 
    
    
    #             check whether tweet is a retweet or not
                if 'RT @' not in text:
                    insertsql = "INSERT OR IGNORE INTO tatorttweets(lfd, screen_name, date, tweet, retweet_count) VALUES (" + str(episodenumber) + ",'" + tweet['user']['screen_name'] + "', '" + str(tweettime) + "', '" + tweet['text'].replace("'", "''") + "', 0)"
                    cur.execute(insertsql)
                    con.commit()
                    self.originalcounter += 1 
    #                 print str(self.originalcounter) + ' ' + tweet['user']['screen_name'].encode('utf-8') + ': ' + tweet['text'].encode('utf-8') + ' (' + str(tweettime) + ')' 
    
                     
                else:
                    
                    lastindex = tweet['text'].rfind('RT @')
                    retweeted_tweet = tweet['text'][lastindex + 3:]
              
                    original_screen_name = retweeted_tweet[retweeted_tweet.find('@') + 1:retweeted_tweet.find(':')]
                    original_tweet = retweeted_tweet[retweeted_tweet.find(':') + 2:]
         
                    
                    if (original_tweet[-1:] == ('...').encode('utf-8')):
                        original_tweet = original_tweet[:-1]
              
                    if "\'" in original_tweet: 
                        original_tweet = original_tweet[:original_tweet.find("\'")]
              
              
                    command = "SELECT id, retweet_count FROM tatorttweets WHERE screen_name = '" + original_screen_name + "' AND tweet LIKE '" + original_tweet + "%'"
                    cur.execute(command)
                    rows = cur.fetchall()
                    if len(rows) == 1: 
                        for row in rows:
                            new_count = (int(row[1]) + 1)
                            command = "UPDATE tatorttweets SET retweet_count = " + str(new_count) + " WHERE id = " + str(row[0])
                            cur.execute(command)
                            con.commit()
                            
                            if new_count == 3: 
                                twitter.create_favorite(id=tweet['id'])
                 
                                         
                    self.retweeted += 1
                    if text not in self.retweets.keys():
                        twitt_times = 1
                    else:
                        twitt_times = self.retweets[text] + 1
                    self.retweets[text] = twitt_times

            
        except Exception,e:
            print 'Exception: ' + str(e)
            sys.stdout.flush()
  

    
    def on_error(self, status_code, data):

        print 'time since start: ' + str(time.time() - start) + ' seconds'
        print 'Error: ' + str(status_code)
        sys.stdout.flush()


with con:
    
    cur = con.cursor()
    command = 'SELECT * FROM metadata ORDER BY lfd DESC LIMIT 10' 
    cur.execute(command)
    rows = cur.fetchall()
    for row in rows:
        print row[0]
        date = datetime.strptime(row[3], '%Y-%m-%d')
        today = date.today()
        
        if today - date >= timedelta(days=0): 
            episodenumber = row[0]
            print 'episodenumber: ' + str(episodenumber)
            print 'date: ' + str(date)
            print 
            generate_all.main(episodenumber, False, False)
            break
        
            
        


stream = MyStreamer(twitterconfig.APP_KEY, twitterconfig.APP_SECRET, twitterconfig.OAUTH_TOKEN, twitterconfig.OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='#Tatort')

