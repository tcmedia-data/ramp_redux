import csv

## File to validate :: Change name 
FXRates_File = "FXRates.csv"

## Companion Files :: Do not change except when new header row is modified
## Script requires FXRates_Headers.csv and BQ_Headers.csv to be in same folder
FXRates_Headers = "FXRates_Headers.csv"
BQ_Headers = "FXRates_Headers.csv"

with open(FXRates_File, "rb") as FXData:
    reader = csv.reader(FXData)
    FXData = reader.next()
    rest = [row for row in reader]
print FXRates_File,'=',FXData
print

with open(FXRates_Headers, "rb") as FXRates_Control:
    reader = csv.reader(FXRates_Control)
    FXRates_Control = reader.next()
    rest = [row for row in reader]
# print DFP_FieldControl,'=', FXRates_Control

with open(BQ_Headers, "rb") as BQ_Control:
    reader = csv.reader(BQ_Control)
    BQ_Control = reader.next()
    rest = [row for row in reader]
# print BQ_FieldOutput,'=',BQ_Control

set1, set2 = set(FXData), set(FXRates_Control)
set3 = set(FXData), set(BQ_Control)

[i for i in FXData if i not in set2]
[i for i in FXRates_Control if i not in set1]
[i for i in FXData if i not in set3]

print
if len([i for i in FXData if i not in FXRates_Control]) <> 0:
    print 'STOP processing:',FXRates_File
    print
    print 'FXRates Column(s) not from FXRates Control File=', ','.join([i for i in FXData if i not in FXRates_Control])
    print 'FXRAtes Column(s) missing in FXRates raw report=', ','.join([i for i in FXRates_Control if i not in BQ_Control and i not in FXData])

else:    
    print 'GO processing:',FXRates_File
