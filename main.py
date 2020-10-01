#
# the links lol

# https://www.ebay.de/sch/i.html?_from=R40&_sacat=0&LH_BIN=1&_nkw=macbook%20pro%2015&LH_Complete=1&LH_Sold=1&rt=nc&_trksid=p2045573.m1684
# bei der suche dann immer mit dem %20 trennen , und statt .bold -> .bold.bidsold
import ebaycrawler

print(""" Der Ebay-Scraper 
-------------------------------------
copyright by Rostimann Iskandrogen 
------------------------------------
Welchen Artikel suchst du ? """)
search = input()
print("Wie viele Artikel sollen verglichen werden ? ")
art_num = int(input())
ebaycrawler.ArticleFetcher().get_prices(search, art_num)

