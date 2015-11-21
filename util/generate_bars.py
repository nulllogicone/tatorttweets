#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-


def main(episodenumber, live_tweet, testmode):
    
    import sqlite3 as lite
    import dateutil.parser
    from twython import Twython 
    import os
    import warnings
    warnings.filterwarnings("ignore")
    import twitterconfig 
    twitter = Twython(twitterconfig.APP_KEY, twitterconfig.APP_SECRET, twitterconfig.OAUTH_TOKEN, twitterconfig.OAUTH_TOKEN_SECRET)

    filename = os.path.join(os.path.dirname(__file__), '../tweets.db')
    con = lite.connect(filename)
    
    with con:
    
        timestring = "" 
    
        cur = con.cursor()
        command = 'SELECT * FROM tatorttweets WHERE lfd = ' + str(episodenumber)

        cur.execute(command)
        rows = cur.fetchall()
    
        for row in rows:
            mydate = dateutil.parser.parse(row[3])
            time = (mydate.hour * 60) + mydate.minute
            if time < 121: 
                time = time + 1440
            
            if (time >= 1200) and (time <= 1320): 
                timestring += str(time) + ", "; 

        filename = os.path.join(dir, "../FlaskWebProject/static/js/plots/bars/bars_template.txt")
        with open (filename, "r") as myfile:
            filestring = myfile.read()
    
        varvalues = 'var values = [ ' + timestring + ' ] '
        if testmode: print varvalues; 
    
        barfilename = os.path.join(dir, "../FlaskWebProject/static/js/plots/bars/bars_" + str(episodenumber) + ".js")
        barfile = open(barfilename, "w")
        print >> barfile, varvalues
        print >> barfile, filestring
        barfile.close()
        
#         cmd = "scp -P 50001 " + barfilename + " kd261@ssh.raumopol.de:../public/tatorttweets/FlaskWebProject/static/js/plots/bars/bars_" + str(episodenumber) + ".js"
#         print cmd
#         os.system(cmd)
        

        tweet = 'Neuer #Tatort Spannungsbogen: http://tatort.mash-it.net/' + str(episodenumber) + '#Verlauf'
        if testmode: print tweet
        if testmode: print len(tweet)
        
        if live_tweet: 
            try:
                twitter.update_status(status=tweet)
            except Exception as e: 
                if testmode: print e
    
if __name__ == "__main__":
    main()
    
    
