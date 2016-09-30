## Script requires DFP_Headers.csv and BQ_Headers.csv to be in same folder

import csv

## File to validate :: Change name 
DFP_File = "DFP_General_20160927.csv" 

## Companion Files :: Do not change except when new header row is modified
DFP_Headers = "DFP_Headers.csv"
BQ_Headers = "BQ_DFP_Headers.csv"

with open(DFP_File, "rb") as DFPData:
    reader = csv.reader(DFPData)
    DFPData = reader.next()
    rest = [row for row in reader]
print DFP_File,'=',DFPData
print

with open(DFP_Headers, "rb") as DFP_Control:
    reader = csv.reader(DFP_Control)
    DFP_Control = reader.next()
    rest = [row for row in reader]
# print DFP_FieldControl,'=', DFP_Control

with open(BQ_Headers, "rb") as BQ_Control:
    reader = csv.reader(BQ_Control)
    BQ_Control = reader.next()
    rest = [row for row in reader]
# print BQ_FieldOutput,'=',BQ_Control

set1, set2 = set(DFPData), set(DFP_Control)
set3 = set(DFPData), set(BQ_Control)

[i for i in DFPData if i not in set2]
[i for i in DFP_Control if i not in set1]
[i for i in DFPData if i not in set3]

print 'DFP Column(s) not from DFP Control File=', ','.join([i for i in DFPData if i not in DFP_Control])
print 'BQ Column(s) missing in DFP raw report=', ','.join([i for i in DFP_Control if i not in BQ_Control and i not in DFPData])

