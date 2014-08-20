#!/usr/bin/python
# -*- coding: utf-8 -*-


import nltk
import sqlite3 as lite
import os
import dateutil.parser
from nltk.corpus import stopwords
from collections import Counter
import urllib2
from bs4 import BeautifulSoup


episodenumber = "913"; 
title = ""
sender = "" 
erstausstrahlung = ""
ermittler = "" 
fall = "" 
highlights = ""


con = lite.connect('../tweets.db')
cnt = Counter()

stop_eng = stopwords.words('english')
stop_ger = stopwords.words('german')
customstopwords = ['tatort', 'mal', 'heute', 'gerade', 'erst', 'macht', 'eigentlich', 'warum', 'gibt', 'gar', 'immer', 'schon', 'beim', 'ganz', 'dass', 'wer', 'mehr', 'gleich', 'wohl']

            
        
        

with con:
    
    timestring = "" 
    
    cur = con.cursor()
    command = 'SELECT * FROM tatorttweets WHERE lfd = ' + episodenumber

    cur.execute(command)
    col_names = [cn[0] for cn in cur.description]
    rows = cur.fetchall()
    
    
    for row in rows:
        mydate = dateutil.parser.parse(row[2])
        time = (mydate.hour * 60) + mydate.minute
        if time < 121: 
            time = time + 1440
            
        if (time >= 1140) and (time <= 1380): 
            timestring += str(time) + ", "; 
            
            cnt[time] += 1
        
#     print timestring
    
    
    counter = cnt.most_common()
    top = counter[:10]
        
    set = []
    for v in top: 
        set.append(v[0])
#         print str(v[0]) + " " + str(v[1])
        
    for s in sorted(set): 
        seconds = s % 60
        if seconds < 10: 
            seconds = "0" + str(seconds)
            
        peaktime = str(s / 60) + ":" + str(seconds)
        peakstring = peaktime + " -"
        
        tokens = []
        tweets = []

        
        select = "SELECT tweet FROM tatorttweets WHERE `date` like '%" + peaktime + "%' AND lfd = " + episodenumber        
        
        cur.execute(select)
        rows = cur.fetchall()

        for row in rows:
            tweets.append(row[0])
            tokens.extend([t.lower().encode('utf-8').strip(":,.!?") for t in row[0].split()])
        
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
    
        vocabulary = freq_dist.keys()
        for v in vocabulary[:5]: 
            peakstring = peakstring + " " + v + " (" + str(freq_dist[v]) + ")"
        
        highlights += peakstring + " <br />\n"
    
    
    print highlights 
 
    
    varvalues = 'var values = [ ' + timestring + ' ] '
    
    print varvalues; 
    
