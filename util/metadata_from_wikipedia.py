#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-



def convertmonth(x):
    return {
        'Mai': 5,
        'Jun.': 6,
        'Aug.': 8,
        'Sep.': 9,
        'Okt.': 10,
        'Nov.': 11,
        'November': 11,
        'Dez.': 12,
        'Jan.': 01,
        'Feb.': 02,
        'März': 03,
        'Mär.': 03,
        'April': 04,
        'Apr.': 04,
        'Juni': 06,
        'Juli': 07,
    }[x]


def main(episodenumber):
        
    import urllib2
    from BeautifulSoup import BeautifulSoup
    import sqlite3 as lite
    import re
    TAG_RE = re.compile(r'<[^>]+>')
    import os
    import argparse
    import datetime
    
    parser = argparse.ArgumentParser()
    parser.add_argument("episodenumber")
    args = parser.parse_args()
    episodenumber = args.episodenumber

    filename = os.path.join(os.path.dirname(__file__), '../tweets.db')
    con = lite.connect(filename)
    

    url = "http://de.wikipedia.org/wiki/Liste_der_Tatort-Folgen"
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    tabulkas = soup.findAll("table", {"class" : "wikitable sortable"})
    
    
    for tabulka in tabulkas: 
        for row in tabulka.findAll('tr'):
            col = row.findAll('td')
            
            if col:
                if (col[0].string == str(episodenumber)):     

                    title = TAG_RE.sub('', str(col[1]))
                    sender = col[2].string
                    erstausstrahlung = TAG_RE.sub('', str(col[3]))
                    ermittler = TAG_RE.sub('', str(col[4]))
                    fall = col[5].string
                    
                    print title
                    print erstausstrahlung
                    elements = erstausstrahlung.split()
                    date = datetime.date(int(elements[2]), convertmonth(elements[1]), int(elements[0].replace('.', '')))
                    print 'date:', date
                    print ermittler
                    
                    with con:
                        cur = con.cursor()
                        insertsql = "INSERT OR IGNORE INTO metadata(lfd, title, sender, erstausstrahlung, ermittler, fall) VALUES (" + str(episodenumber) + ", '" + str(title) + "', '" + str(sender) + "', '" + str(date) + "', '" + ermittler + "', " + str(fall) + ")"
                        cur.execute(insertsql)
                        con.commit()
                        

if __name__ == "__main__":
    main("941")
    