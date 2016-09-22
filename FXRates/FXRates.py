##http://lxml.de/parsing.html#parsing-html

import lxml
from lxml import etree,html
from lxml.etree import XMLParser
import scraperwiki
import csv
from subprocess import Popen

URL="http://www.bankofcanada.ca/rates/exchange/usd-can-summary/"

parser = XMLParser(ns_clean=True, recover=True)
doc = lxml.html.fromstring(scraperwiki.scrape(URL))

FXRates = doc.xpath('//*[@class="table-responsive"]/*[@class="table table-bordered table-hover"]/tr[3]/td/text()')
FXList=[x.strip() for x in FXRates]
print FXList

Headers=["Date", "USD2CAD", "CAD2USD"]
with open('FXUSD2CAD.csv', 'wb') as MyHeaders:
    writer = csv.DictWriter(MyHeaders, delimiter=";",fieldnames=Headers)
    writer.writeheader()
    MyHeaders.close()

with open('FXUSD2CAD.csv', 'a') as MyRates:
    writer = csv.writer(MyRates, delimiter=";", quoting=csv.QUOTE_ALL)
    writer.writerow(FXList)
    MyRates.close()

p = Popen('FXUSD2CAD.csv', shell=True)
