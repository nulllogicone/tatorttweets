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

    
    top_retweets = '' 
    striketweet = '#Tatort - Ins Schwarze getwittert: '
    top_tweeters = [] 
    
    
    with con:
        
        cur = con.cursor()
        command = 'SELECT * FROM tatorttweets WHERE lfd =  ' + str(episodenumber) + ' ORDER BY retweet_count DESC LIMIT 10' 

        cur.execute(command)
        rows = cur.fetchall()
        for row in rows:
            if testmode: print row[2]
            
            newtweet = striketweet + ' \n@' + row[2] 
            if not ((len(newtweet) > 140) or (row[2] in top_tweeters)): 
                striketweet = newtweet 
                top_tweeters.append(row[2])
            try: 
                twitter.create_friendship(screen_name=row[2])
            except Exception as e: 
                if testmode: print e

            if testmode: print row[4]

            searchstring = '"' + row[4] + '"'

            response = twitter.search(q=searchstring, include_entities=1, count=100)
            for tweet in response['statuses']: 
                if 'RT @' not in tweet['text'] and (row[2] == tweet['user']['screen_name']): 
                    oembed = twitter.get_oembed_tweet(id=tweet['id'])
#                     print oembed['html']
                    try: 
                        twitter.create_favorite(id=tweet['id'])
                    except Exception as e: 
                        if testmode: print e

                    top_retweets += oembed['html'].encode('utf-8') + " <br />\n"
                
        
        topretweetsfilename = os.path.join(dir, "../FlaskWebProject/templates/top_retweets/top_retweets_" + str(episodenumber) + ".txt")
        topretweetsfile = open(topretweetsfilename, "w")
#         print top_retweets 
        print >> topretweetsfile, top_retweets
        topretweetsfile.close()
        
#         cmd = "scp -P 50001 " + topretweetsfilename + " kd261@ssh.raumopol.de:../public/tatorttweets/FlaskWebProject/templates/top_retweets/top_retweets_" + str(episodenumber) + ".txt"
#         print cmd
#         os.system(cmd)
        
        if testmode: print 
        if testmode: print striketweet
        if testmode: print len(striketweet)
        
        
        
        if live_tweet: 
            try:
                twitter.update_status(status=striketweet)
                twitter.update_status(status="Die meist-retweeted #Tatort tweets: http://tatort.mash-it.net/" + str(episodenumber) + "#Strike")
            except Exception as e: 
                if testmode: print e

if __name__ == "__main__":
    main()
    
    
    
