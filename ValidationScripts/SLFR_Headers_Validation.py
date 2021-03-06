import csv
import datetime

# Get the current date and time
now = datetime.datetime.now()
now_str = now.strftime("%Y%m%d")

## File to validate :: Change name 
SLFR_siteMapping_File = "SiteMapping_20160930.csv"
# OR USE 
# SLFR_siteMapping_File = "SiteMapping_"+str(datetime.datetime.now().strftime('%Y%m%d'))+".csv"

## Companion Files :: Do not change except when new header row is modified
## Script requires DFP_Headers.csv and BQ_Headers.csv to be in same folder
SLFR_Headers = "siteMapping_Headers.csv"
BQ_Headers = "BQ_siteMapping_Headers.csv"

with open(SLFR_siteMapping_File, "rb") as SLFRData:
    reader = csv.reader(SLFRData,delimiter=',')
    SLFRData = reader.next()
    rest = [row for row in reader]
print SLFR_siteMapping_File,'=',SLFRData
print

with open(SLFR_Headers, "rb") as SLFR_Control:
    reader = csv.reader(SLFR_Control,delimiter=',')
    SLFR_Control = reader.next()
    rest = [row for row in reader]
# print SLFR_Headers,'=', SLFR_Control


with open(BQ_Headers, "rb") as BQ_Control:
    reader = csv.reader(BQ_Control,delimiter=',')
    BQ_Control = reader.next()
    rest = [row for row in reader]
# print BQ_Headers,'=',BQ_Control

set1, set2 = set(SLFRData), set(SLFR_Control)
set3 = set(SLFRData), set(BQ_Control)

[i for i in SLFRData if i not in set2]
[i for i in SLFR_Control if i not in set1]
[i for i in SLFRData if i not in set3]

print
if len([i for i in SLFRData if i not in SLFR_Control]) <> 0:
    print 'STOP processing:',SLFR_siteMapping_File
    print
    print 'SLFR Column(s) not from SLFR Control File=', ','.join([i for i in SLFRData if i not in SLFR_Control])
    print 'BQ Column(s) missing in SLFR raw report=', ','.join([i for i in SLFR_Control if i not in BQ_Control and i not in SLFRData])

else:    
    print 'GO processing:',SLFR_siteMapping_File

