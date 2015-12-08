#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import generate_bars 
import generate_wordcloud 
import generate_top_retweets 
import generate_top_tweeters 
import warnings
warnings.filterwarnings("ignore")



import sqlite3 as lite
from datetime import datetime, timedelta
import os

episodenumber = 964
testmode = True
live_tweet = False 

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../tweets.db')
con = lite.connect(filename)


def main():
    with con:
        cur = con.cursor()
        command = 'SELECT * FROM metadata ORDER BY lfd DESC LIMIT 10' 
        cur.execute(command)
        rows = cur.fetchall()
        for row in rows:
            date = datetime.strptime(row[3], '%Y-%m-%d')
            today = date.today()
            if today-date >= timedelta(days=0): 
                if testmode: print date
                episodenumber = row[0]
                break

    episodenumber = 964
    # 
    # if testmode: print episodenumber
    # if testmode: print live_tweet
        
    # for episodenumber in xrange(910,927,1): 
    #     print episodenumber
    
    generate_wordcloud.main(episodenumber, live_tweet, testmode)
    generate_bars.main(episodenumber, live_tweet, testmode)
    generate_top_retweets.main(episodenumber, live_tweet, testmode)
    generate_top_tweeters.main(episodenumber, live_tweet, testmode)


if __name__ == "__main__":
    main()
