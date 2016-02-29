#!/usr/local/Trin/python2.7
# -*- coding: utf-8 -*-


from twython import Twython    
import sqlite3 as lite
import nltk
from nltk.collocations import *
import random
from nltk.corpus import stopwords
import os
from pprint import pprint
import csv
import sys
import warnings
warnings.filterwarnings("ignore")


def main(episodenumber, live_tweet, testmode):
    
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, '../tweets.db')
    con = lite.connect(filename)

    import twitterconfig 
    twitter = Twython(twitterconfig.APP_KEY, twitterconfig.APP_SECRET, twitterconfig.OAUTH_TOKEN, twitterconfig.OAUTH_TOKEN_SECRET)

    
    stop_eng = stopwords.words('english')
    stop_ger = stopwords.words('german')
    customstopwords = ['#tatort', 'tatort', 'mal', 'heute', 'gerade', 'erst', 'macht', 'eigentlich', 'ach', 'warum', 'gibt', 'gar', 'immer', 'schon', 'beim', 'ganz', 'dass', 'wer', 'mehr', 'gleich', 'wohl']

    tokens = []
    tweets = [] 

    with con:
        
        cur = con.cursor()    
        command = 'SELECT * FROM tatorttweets WHERE lfd = ' + str(episodenumber)
    
        cur.execute(command)
        
        rows = cur.fetchall()
    
        for row in rows:
            tweets.append(row[4].encode('utf-8'))
            tokens.extend([t.lower().encode('utf-8').strip(":,.!?") for t in row[4].split()])
        
        hashtags = [w for w in tokens if w.startswith('#')]
        mentions = [w for w in tokens if w.startswith('@')]
        links = [w for w in tokens if w.startswith('http') or w.startswith('www')]
    
        filtered_tokens = [w for w in tokens \
        if not w in stop_eng \
        and not w in stop_ger \
        and not w in customstopwords \
        and not len(w) < 3 \
        and not w in links] 
        
#         and w.isalpha() \
#         and not w in hashtags \       
#        and not w in mentions]
    
        freq_dist = nltk.FreqDist(filtered_tokens)
        
        
    
        cloudstring = ""; 
        vocabulary = freq_dist.keys()
        for v in vocabulary[:85]: 
            
            string = str(freq_dist[v]).replace("\"", "")
                    
            if  (bool(random.getrandbits(1))): 
                cloudstring = cloudstring + "{text: \"" + v + "\", weight: " + string + "}, \n"
            else: 
                cloudstring = cloudstring + "{text: \"" + v + "\", weight: " + string + " , html: {\"class\": \"vertical\"}}, \n"
        if testmode: print cloudstring
        cloudstring = cloudstring.replace("\"\"", "\"")
    
    
        wordcloudfilename = os.path.join(dir, "../FlaskWebProject/static/js/plots/cloud/cloud_" + str(episodenumber) + ".js")
        wordcloudfile = open(wordcloudfilename, "w")
        print >> wordcloudfile, 'var word_list = [' 
        print >> wordcloudfile, cloudstring
        print >> wordcloudfile, '];\n$(function() {\n$("#cloud").jQCloud(word_list);\n});' 
        wordcloudfile.close()

#         cmd = "scp -P 50001 " + wordcloudfilename + " kd261@ssh.raumopol.de:../public/tatorttweets/FlaskWebProject/static/js/plots/cloud/cloud_" + str(episodenumber) + ".js"
#         print cmd
#         os.system(cmd)
        
        
        tweet = 'Neue #Tatort Twitterwolke: http://tatort.mash-it.net/' + str(episodenumber) + '#Cloud'
        if testmode: print tweet
        if testmode: print len(tweet)
        
        if live_tweet: 
            try: 
                twitter.update_status(status=tweet)
            except Exception as e: 
                if testmode: print e 
    

        if (False): 
            trigram_measures = nltk.collocations.TrigramAssocMeasures()
            finder = TrigramCollocationFinder.from_words(filtered_tokens)
    
            tritweet = "Top #Tatort Trigrams: \n"
    
            for i in finder.nbest(trigram_measures.pmi, 10): 
                nicestring = i[0] + " " + i[1] + " " + i[2]
                nicestring = nicestring.replace("\"", "")
                newtritweet = tritweet + nicestring + "\n"
                if len(newtritweet) <= 140: 
                    tritweet = newtritweet 
                if testmode: print nicestring
            
            if testmode: print 
            if testmode: print newtritweet
    #         if live_tweet: 
    #             try: 
    #                 twitter.update_status(status=tritweet)
    #             except Exception as e: 
    #                 print e 
                
    
    
            
            training_set=[]
    
    
            poswords = csv.reader(open(os.path.join(dir, '../SentiWS_v1.8c/SentiWS_v1.8c_Positive.txt'), 'rb'), delimiter='|')
            training_set.extend([(pos[0].lower(), 'positive') for pos in poswords])
    
            negwords = csv.reader(open(os.path.join(dir, '../SentiWS_v1.8c/SentiWS_v1.8c_Negative.txt'), 'rb'), delimiter='|')
            training_set.extend([(neg[0].lower(), 'negative') for neg in negwords])
            
    
            pos_tweet = ['Das war ein guter', \
                 'Spitze', \
                 'Guter', \
                 'spannend bis zum schluss', \
                 'bester tatort seit langem', \
                 'top', \
                 'Ein skurriler tatort heut. #ilike', \
                 'erstaunlich guter', \
                 u'Wirklich überraschend dieser', \
                 'Grandios']
    
            neg_tweet = ['Langweilig', \
                 u'Blöder', \
                 'umschalten', \
                 'er soll sterben', \
                 'abschalten bei dem mist', \
                 u'absehbar, wer der mörder ist', \
                 'was will dieser justin bieber', \
                 u'Ich hab so ein ungutes Gefühl', \
                 'justin bieber', \
                 'so ein praktikant mit der waffe', \
                 'was will dieser bubi', \
                 u'Warum tragen die Frauen im heutigen Tatort so miese Perücken?', \
                 u'Ja, diese Musik stört', \
                 'Ich schalte um']
    
    
            
            samples = freq_dist.keys()[:2000]
            if testmode: print samples[:10]
            if testmode: print('We have %s samples.' % len(samples))
    
    
    
            def tweet_features(tweet):
                features={}
                for word in samples:
                    features['contains(%s)' % word.decode('utf-8')] = (word in tweet)
                return features
    
            trainingfeatureset = [(tweet_features(word), sentiment) for (word, sentiment) in training_set]
            classifier = nltk.NaiveBayesClassifier.train(trainingfeatureset)
            classifier.show_most_informative_features(14)
            
            positivtweets = []
            negativtweets = []
            for tweet in tweets:
                ts = classifier.classify(tweet_features(tweet))
                if ts=='positive':
                    positivtweets.append(tweet)
                else:
                    negativtweets.append(tweet)
                    
            if testmode: print 'positive: ' + str(len(positivtweets))
            if testmode: print 'negative: ' + str(len(negativtweets))
            if testmode: print 'all together: ' + str(len(tweets))



if __name__ == "__main__":
    main(964, False, True)   
    
