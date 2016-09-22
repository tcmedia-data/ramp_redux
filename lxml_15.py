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
##elem2 = doc.xpath('//*[@class="table-responsive"]/*[@class="table table-bordered table-hover"]/tr[3]/td[1]/text()')
##elem3 = doc.xpath('//*[@class="table-responsive"]/*[@class="table table-bordered table-hover"]/tr[3]/td[2]/text()')
##elem4 = doc.xpath('//*[@class="table-responsive"]/*[@class="table table-bordered table-hover"]/tr[3]/td[3]/text()')
FXList=[x.strip() for x in FXRates]
##print [x.strip() for x in elem2]
##print [x.strip() for x in elem3]
##print [x.strip() for x in elem4]
##print FXList
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
