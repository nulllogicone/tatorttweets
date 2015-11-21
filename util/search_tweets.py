#!/usr/bin/python
# -*- coding: utf-8 -*-

from twython import Twython
import time 
from datetime import datetime, timedelta
import sqlite3

global countTweets
global maxID
global done
 

# http://www.tatort-fundus.de/web/rangliste/folgen-wertungen/rangliste-auswertung/aktueller-zeitpunkt.html
lfd = 962
dateFrom = '2015-11-15';  # Inclusive (YYYY-MM-DD)
dateTo = '2015-11-16';  # Exclusive (YYYY-MM-DD)
keyword = '#Tatort'; 
tweetsXiteration = 100;  # Where 100 is the max


import twitterconfig 
twitter = Twython(twitterconfig.APP_KEY, twitterconfig.APP_SECRET, twitterconfig.OAUTH_TOKEN, twitterconfig.OAUTH_TOKEN_SECRET)


def query_and_process_results():
    
    global countTweets
    global maxID
    global done
    
    oldMaxID = maxID

    timeofinterest = datetime(2015, 11, 15, 20, 00)
    timeofinterest += timedelta(hours=1) # winter time

    if (maxID == 0): 
        response = twitter.search(q=keyword, lang="de", count=tweetsXiteration,
                              since=dateFrom, until=dateTo,
                              include_entities=1, result_type='recent');   

    else: 
        response = twitter.search(q=keyword, lang="de", count=tweetsXiteration,
                              since=dateFrom, until=dateTo, max_id=maxID,
                              include_entities=1, result_type='recent');   

    for tweet in response['statuses']:
        
        mytime = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        mytime += timedelta(hours=1)
        
        print "id_str: " + tweet['id_str']
        print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), str(mytime))
        print tweet['text'].encode('utf-8'), '\n'
        
        insertsql = "INSERT INTO tatorttweets(lfd, screen_name, date, tweet) VALUES (" + str(lfd) + ",'" + tweet['user']['screen_name'] + "', '" + str(mytime) + "', '" + tweet['text'].replace("'", "''") + "')"
        c.execute(insertsql)
        conn.commit()
        maxID = int(tweet['id_str']) - 1

    if (oldMaxID == maxID) or (mytime < timeofinterest): 
        done = 'true'
        print 'done!!!!'

    countTweets = countTweets + len(response['statuses']);
    print "countTweets: " + str(countTweets) 



conn = sqlite3.connect('../tweets.db')
c = conn.cursor()
conn.commit()



countTweets = 0 
maxID = 0
done = 'false'; 


query_and_process_results()


while (done == 'false'):

    print ("Time to sleep")
    time.sleep(60)
    
    query_and_process_results()
    
conn.close()
