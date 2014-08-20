from twython import Twython
import time 
import sqlite3
from datetime import datetime, timedelta


global countTweets
global maxID
global done
 
        
# http://www.tatort-fundus.de/web/rangliste/folgen-wertungen/rangliste-auswertung/aktueller-zeitpunkt.html
lfd = 913
dateFrom = '2014-06-09';  # Inclusive (YYYY-MM-DD)
dateTo = '2014-06-10';  # Exclusive (YYYY-MM-DD)
keyword = '#tatort'; 
tweetsXiteration = 100;  # Where 100 is the max


# aimash
APP_KEY = "*****"
APP_SECRET = "*****"
OAUTH_TOKEN = "*****"
OAUTH_TOKEN_SECRET = "*****"
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)



def query_and_process_results():
    
    global countTweets
    global maxID
    global done
    
    oldMaxID = maxID

    timeofinterest = datetime(2014, 05, 04, 14, 00)

    
    if (maxID == 0): 
        response = twitter.search(q=keyword, lang="de", count=tweetsXiteration,
                              since=dateFrom, until=dateTo,
                              include_entities=1, result_type='recent');   
                              
    else: 
        response = twitter.search(q=keyword, lang="de", count=tweetsXiteration,
                              since=dateFrom, until=dateTo, max_id=maxID,
                              include_entities=1, result_type='recent');   
        
    
    for tweet in response['statuses']:
        print "id_str: " + tweet['id_str']
        print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
        print tweet['text'].encode('utf-8'), '\n'
        mytime = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        mytime += timedelta(hours=2)
        insertsql = "INSERT INTO tatorttweets(lfd, screen_name, date, tweet) VALUES (" + str(lfd) + ",'" + tweet['user']['screen_name'] + "', '" + str(mytime) + "', '" + tweet['text'].replace("'", "''") + "')"
        c.execute(insertsql)
        conn.commit()
        maxID = int(tweet['id_str']) - 1

    countTweets = countTweets + len(response['statuses']);
    print "countTweets: " + str(countTweets) 
    
    if (oldMaxID == maxID) or (mytime.time() < timeofinterest.time()): 
        done = 'true';



conn = sqlite3.connect('../tweets.db')
c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS tweets
#              (lfd INTEGER, screen_name text, date text, tweet text)''')
conn.commit()



countTweets = 0 
maxID = 475849288849698816
done = 'false'; 

     
query_and_process_results()


while (done == 'false'):

    print ("Time to sleep")
    time.sleep(60)
    
    query_and_process_results()
    
conn.close()
