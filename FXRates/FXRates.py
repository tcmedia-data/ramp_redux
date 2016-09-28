##http://stackoverflow.com/questions/17693972/python-header-print-one-time-for-every-time-i-run-the-script-not-each-time
##http://lxml.de/parsing.html#parsing-html


import lxml
from lxml import etree,html
from lxml.etree import XMLParser
import scraperwiki
import csv
from subprocess import Popen


URL="http://www.bankofcanada.ca/rates/exchange/usd-can-summary/"
FXFile="FXRates.csv"

parser = XMLParser(ns_clean=True, recover=True)
doc = lxml.html.fromstring(scraperwiki.scrape(URL))

FXRates = doc.xpath('//*[@class="table-responsive"]/*[@class="table table-bordered table-hover"]/tr[3]/td/text()')
FXList=[x.strip() for x in FXRates]
print FXList

#--- Open the file   + write on it ---
fx = open(FXFile,'a')
prev_data = open(FXFile, 'r').read()

header = "FXDate,USD2CAD,CAD2USD\n"

# Add a header only if the file is empty
if prev_data == '':
    fx.write(','.join(header))

fx.write(','.join(FXList))
fx.write('\n')
fx.close()
# --- And Close the file ---

#p = Popen(FXFile, shell=True)
