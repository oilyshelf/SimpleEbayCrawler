import time
import requests
from bs4 import BeautifulSoup
import re
from .Article import Article


class ArticleFetcher:
    def fetch(self, suchbegriff, art):
        indexurl = "https://www.ebay.de/sch/i.html?_from=R40&_sacat=0&_nkw={}&rt=nc&LH_BIN=1" if art else "https://www.ebay.de/sch/i.html?_from=R40&_sacat=0&LH_BIN=1&_nkw={}&LH_Complete=1&LH_Sold=1&rt=nc&_trksid=p2045573.m1684"
        seperator = "+" if art else "%20"
        formatted_string = suchbegriff.replace(" ", seperator)
        item_selector = ".bold" if art else ".bold.bidsold"
        url = indexurl.format(formatted_string)
        counter = 1

        while url != "":
            counter += 1
            print(url)
            time.sleep(1)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")

            results = doc.select(".sresult.lvresult.clearfix.li")
            for li in results:
                res = li.select(".lvprice.prc")
                link_item = li.select_one("a.vip").attrs["href"]
                for item in res:
                    fastda = item.select(item_selector)
                    for price in fastda:
                        temp = re.findall("\d{0,3}[.]{0,1}\d{1,3}[,]\d{1,2}", price.text)
                        temp = temp[0].replace(".", "")
                        temp = temp.replace(",", ".")
                        yield Article(link_item, float(temp))

            for page in doc.select("a.pg"):
                if page.text == str(counter):
                    url = page.attrs["href"]
                    break

    def get_prices(self, suchbegriff, number_articles=50):
        result_buy = []
        result_sell = []
        print("Links der gescrapten Websiten :")
        buy_generator = self.fetch(suchbegriff, True)
        sell_generator = self.fetch(suchbegriff, False)
        for i in range(number_articles):
            result_buy.append(next(buy_generator))
            result_sell.append(next(sell_generator))

        result_buy.sort()
        result_sell.sort()
        print("Durchschnittlicher Kauf Preis bei ", number_articles, "Artikel")
        print(sum(result_buy)/len(result_buy), "€")
        print("Billigster und Teuerster Artikel : ")
        print(result_buy[0])
        print(result_buy[-1])

        print("Durchschnittlicher Verkaufs Preis bei ", number_articles, "Artikel")
        print(sum(result_sell)/len(result_sell), "€")
        print("Billigster und Teuerster Artikel : ")
        print(result_sell[0])
        print(result_sell[-1])
