#!/usr/bin/python
# -*- coding: utf-8 -*-


import sqlite3 as lite

found = 0
con = lite.connect('../../tweets.db')

with con:
    cur = con.cursor()



#     1) create new table
#     command = 'CREATE TABLE tweets_clean (id INTEGER PRIMARY KEY, lfd NUMERIC, screen_name TEXT, date NUMERIC, tweet TEXT, retweet_count NUMERIC);' 
#     cur.execute(command)

#     2) alles außer aktueller nummer kopieren 
#     command = 'INSERT INTO tweets_clean SELECT * FROM tatorttweets WHERE lfd != 962;' 
#     cur.execute(command)

#   4) alles außer aktueller nummer kopieren 
#     command = "UPDATE tweets_clean SET retweet_count = 0 WHERE retweet_count = 'None'" 
#     cur.execute(command)

#   6) table tatorttweets löschen
#     command = "DROP TABLE tatorttweets" 
#     cur.execute(command)
    
    
#     7) neue Tabelle umbenennen
#     command = "ALTER TABLE tweets_clean RENAME TO tatorttweets;" 
#     cur.execute(command)
    
#    3) & 5) durch alle tweets gehen 
#     command = 'SELECT * FROM tatorttweets WHERE lfd == 962' 
#     cur.execute(command)
#     rows = cur.fetchall()
#     for row in rows:
#         
# #       3) originale speichern 
#         if not 'RT @' in row[4]:   
#             insertsql = "INSERT INTO tweets_clean(lfd, screen_name, date, tweet, retweet_count) VALUES (" + str(row[1]) + ",'" + row[2] + "', '" + row[3] + "', '" + row[4].replace("'", "''") + "', '" + str(row[5]) + "')"
#             cur.execute(insertsql)
#             con.commit()

     
#       5) retweets updaten 
#         if  'RT @' in row[4]:
#    
#             lastindex = row[4].rfind('RT @')
#             retweeted_tweet = row[4][lastindex + 3:]
#                 
#             original_screen_name = retweeted_tweet[retweeted_tweet.find('@') + 1:retweeted_tweet.find(':')]
#             original_tweet = retweeted_tweet[retweeted_tweet.find(':') + 2:]
#                 
#             if (original_tweet[-1:] == unicode('...')):
#                 original_tweet = original_tweet[:-1]
#                 
#             if "\'" in original_tweet: 
#                 original_tweet = original_tweet[:original_tweet.find("\'")]
#                 
#             command = "SELECT id, retweet_count FROM tweets_clean WHERE screen_name = '" + original_screen_name + "' AND tweet LIKE '" + original_tweet + "%'"
#             cur.execute(command)
#             rows = cur.fetchall()
#             if len(rows) == 1: 
#                 found += 1
#                 for row in rows:
#                     new_count = (int(row[1]) + 1)
#                     command = "UPDATE tweets_clean SET retweet_count = " + str(new_count) + " WHERE id = " + str(row[0])
#                     cur.execute(command)
#                     con.commit()
        
con.commit 
con.close 
