import urllib2
from BeautifulSoup import BeautifulSoup
import sqlite3 as lite
import re

TAG_RE = re.compile(r'<[^>]+>')
con = lite.connect('../tweets.db')

episodenumber = "913" 
title = ""
sender = "" 
erstausstrahlung = ""
ermittler = "" 
fall = "" 

url = "http://de.wikipedia.org/wiki/Liste_der_Tatort-Folgen"
soup = BeautifulSoup(urllib2.urlopen(url).read())
tabulka = soup.find("table", {"class" : "wikitable sortable"})



def remove_tags(text):
    return TAG_RE.sub('', text)

for row in tabulka.findAll('tr'):
    col = row.findAll('td')
    
    if col:        
        if (col[0].string == episodenumber):     
            
            print row
            title = remove_tags(str(col[1]))
            sender = col[2].string
            erstausstrahlung = remove_tags(str(col[3]))
            ermittler = remove_tags(str(col[4]))
            fall = col[5].string
            
            print title
            print erstausstrahlung
            print ermittler
            
            with con:
                cur = con.cursor()
            
                insertsql = "INSERT OR IGNORE INTO metadata(lfd, title, sender, erstausstrahlung, ermittler, fall) VALUES (" + str(episodenumber) + ", '" + str(title) + "', '" + str(sender) + "', '" + str(erstausstrahlung) + "', '" + ermittler + "', " + str(fall) + ")"
                print (insertsql);
                cur.execute(insertsql)
                con.commit()
