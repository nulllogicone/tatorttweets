#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

def main(episodenumber, live_tweet, testmode):
    
    import sqlite3 as lite
    from twython import Twython
    import os
    import warnings
    warnings.filterwarnings("ignore")

    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, '../tweets.db')
    con = lite.connect(filename)
    
    import twitterconfig 
    twitter = Twython(twitterconfig.APP_KEY, twitterconfig.APP_SECRET, twitterconfig.OAUTH_TOKEN, twitterconfig.OAUTH_TOKEN_SECRET)


    top_tweets = '' 
    tweet = '#Tatort Twitter-SEK: '
    
    with con:
        
        cur = con.cursor()
        command = 'SELECT screen_name, count(tweet) FROM tatorttweets WHERE lfd = ' + str(episodenumber) + ' GROUP BY screen_name ORDER BY count(tweet) desc LIMIT 10 ' 

        cur.execute(command)
        rows = cur.fetchall()
        for row in rows:
            try: 
                twitter.create_friendship(screen_name=row[0])
            except Exception as e: 
                if testmode: print e
            stringrow = '<a href="http://twitter.com/' + row[0] + '">@' + row[0] + '</a>' + ' (' + str(row[1]) + ')'
            top_tweets += stringrow + " <br />\n"
            newtweet = tweet + ' \n@' +  row[0] 
            if not len(newtweet) > 140: 
                tweet = newtweet 

        toptweetsfilename = os.path.join(dir, "../FlaskWebProject/templates/top_tweets/top_tweets_" + str(episodenumber) + ".txt")
        toptweetsfile = open(toptweetsfilename, "w")
        if testmode: print top_tweets 
        print >> toptweetsfile, top_tweets
        toptweetsfile.close()
        
#         cmd = "scp -P 50001 " + toptweetsfilename + " kd261@ssh.raumopol.de:../public/tatorttweets//FlaskWebProject/templates/top_tweets/top_tweets_" + str(episodenumber) + ".txt"
#         print cmd
#         os.system(cmd)
        
        if testmode: print 
        if testmode: print tweet
        if testmode: print len(tweet)
        
        if live_tweet: 
            try: 
                twitter.update_status(status=tweet)
            except Exception as e: 
                if testmode: print e


if __name__ == "__main__":
    main(962, False, True)           


