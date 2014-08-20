# -*- coding: utf-8 -*-

import sqlite3 as lite
import nltk
import random
from nltk.corpus import stopwords

episodenumber = "886"; 
con = lite.connect('../tweets.db')

stop_eng = stopwords.words('english')
stop_ger = stopwords.words('german')
customstopwords = ['tatort', 'mal', 'heute', 'gerade', 'erst', 'macht', 'eigentlich', 'warum', 'gibt', 'gar', 'immer', 'schon', 'beim', 'ganz', 'dass', 'wer', 'mehr', 'gleich', 'wohl']

tokens = []
tweets = []

with con:
        
    cur = con.cursor()    
    command = 'SELECT * FROM tatorttweets WHERE lfd = ' + episodenumber
    
    cur.execute(command)
    
    col_names = [cn[0] for cn in cur.description]
    
    rows = cur.fetchall()
    
    for row in rows:
        tweets.append(row[3])
        tokens.extend([t.lower().encode('utf-8').strip(":,.!?") for t in row[3].split()])
        
    hashtags = [w for w in tokens if w.startswith('#')]
    mentions = [w for w in tokens if w.startswith('@')]
    links = [w for w in tokens if w.startswith('http') or w.startswith('www')]
    
    filtered_tokens = [w for w in tokens \
                   if not w in stop_eng \
                   and not w in stop_ger \
                   and not w in customstopwords \
                   and w.isalpha() \
                   and not len(w) < 3 \
                   and not w in hashtags \
                   and not w in links \
                   and not w in mentions]
    
    freq_dist = nltk.FreqDist(filtered_tokens)
    
    cloudstring = ""; 
    vocabulary = freq_dist.keys()
    for v in vocabulary[:30]: 
        
        if  (bool(random.getrandbits(1))): 
            cloudstring = cloudstring + "{text: \"" + v + "\", weight: " + str(freq_dist[v]) + "}, \n"
        else: 
            cloudstring = cloudstring + "{text: \"" + v + "\", weight: " + str(freq_dist[v]) + " , html: {\"class\": \"vertical\"}}, \n"
    print cloudstring
    
   
    
    
    
   
    
    
#     print
#     
#     tweettext = nltk.Text(filtered_tokens)
#     print tweettext.similar("ballauf")

    
