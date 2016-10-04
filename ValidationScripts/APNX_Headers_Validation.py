import csv

## File to validate :: Change name 
APNX_File = "APPNEXUS_NETWORK_20160927.csv"

## Companion Files :: Do not change except when new header row is modified
## Script requires DFP_Headers.csv and BQ_Headers.csv to be in same folder
APNX_Headers = "APNX_Headers.csv"
BQ_Headers = "BQ_APNX_Headers.csv"

with open(APNX_File, "rb") as APNXData:
    reader = csv.reader(APNXData,delimiter=';')
    APNXData = reader.next()
    rest = [row for row in reader]
print APNX_File,'=',APNXData
print

with open(APNX_Headers, "rb") as APNX_Control:
    reader = csv.reader(APNX_Control,delimiter=';')
    APNX_Control = reader.next()
    rest = [row for row in reader]
# print APNX_Headers,'=', APNX_Control


with open(BQ_Headers, "rb") as BQ_Control:
    reader = csv.reader(BQ_Control,delimiter=';')
    BQ_Control = reader.next()
    rest = [row for row in reader]
# print BQ_Headers,'=',BQ_Control

set1, set2 = set(APNXData), set(APNX_Control)
set3 = set(APNXData), set(BQ_Control)

[i for i in APNXData if i not in set2]
[i for i in APNX_Control if i not in set1]
[i for i in APNXData if i not in set3]

print
if len([i for i in APNXData if i not in APNX_Control]) <> 0:
    print 'STOP processing:',APNX_File
    print
    print 'APNX Column(s) not from APNX Control File=', ','.join([i for i in APNXData if i not in APNX_Control])
    print 'BQ Column(s) missing in APNX raw report=', ','.join([i for i in APNX_Control if i not in BQ_Control and i not in APNXData])
else:    
    print 'GO processing:',APNX_File

