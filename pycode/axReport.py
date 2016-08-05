from nexusadspy import AppnexusReport
import json
import csv
import sys, getopt
def buildReport(startDate, endDate, outfile, bruFile):
    columns = ["day",
               "publisher_name",
               "publisher_id",
               "placement_name",
               "placement_id",
               "site_name",
               "site_id",
               "buyer_member_name",
               "buyer_member_id",
               "seller_member_name",
               "seller_member_id",
               "advertiser_name",
               "advertiser_id",
               "line_item_name",
               "line_item_id",
               "campaign_id",
               "campaign_name",
               "bid_type",
               "advertiser_currency",
               "publisher_currency",
               "imp_type",
               "campaign_priority",
               "media_type",
               "line_item_type",
               "payment_type",
               "revenue_type",
               "imps",
               "clicks",
               "total_convs",
               "revenue",
               "revenue_buying_currency"]

    report_type = "network_analytics"
    SEMI = ';'

    report = AppnexusReport(start_date=startDate,
                            end_date=endDate,
                            report_type=report_type,
                            columns=columns)
    output_json = report.get()
    bru_output = csv.DictWriter(open(bruFile, 'w', newline=''), fieldnames=columns,delimiter=';',quoting = csv.QUOTE_MINIMAL)
    output = open(outfile , 'w', newline='')
    output.write (';'.join(columns) + '\n')
    for row in output_json:
        line = row['day'] + SEMI + row['publisher_name'].replace(',','').replace(';','') \
               + SEMI + row['publisher_id'] \
               + SEMI + row['placement_name'].replace(',','').replace(';','')\
               + SEMI + row['placement_id']\
               + SEMI + row['site_name'].replace(',','').replace(';','')\
               + SEMI + row['site_id']\
               + SEMI + row['buyer_member_name'].replace(',','').replace(';','')\
               + SEMI + row['buyer_member_id']\
               + SEMI + row['seller_member_name'].replace(',','').replace(';','')\
               + SEMI + row['seller_member_id']\
               + SEMI + row['advertiser_name'].replace(',','').replace(';','')\
               + SEMI + row['advertiser_id']\
               + SEMI + row['line_item_name'].replace(',','').replace(';','')\
               + SEMI + row['line_item_id']\
               + SEMI + row['campaign_id']\
               + SEMI + row['campaign_name'].replace(',','').replace(';','')\
               + SEMI + row['bid_type'] \
               + SEMI + row['advertiser_currency'] \
               + SEMI + row['publisher_currency']\
               + SEMI + row['imp_type']\
               + SEMI + row['campaign_priority']\
               + SEMI + row['media_type']\
               + SEMI + row['line_item_type']\
               + SEMI + row['payment_type']\
               + SEMI + row['revenue_type']\
               + SEMI + row['imps']\
               + SEMI + row['clicks']\
               + SEMI + row['total_convs']\
               + SEMI + row['revenue']\
               + SEMI + row['revenue_buying_currency']

        line= line.replace(';Inc',' Inc')\
                .replace(';LLC',' LLC')\
                .replace('TheRichest.com;TheSportster.com;Thetalko.com;Screenrant.com','TheRichest.com-TheSportster.com-Thetalko.com-Screenrant.com')\
                .replace('sportingz.com;semesterz.com','sportingz.com-semesterz.com' )\
                .replace('Viewmixed.com;Zonable.com;Boreburn.com;uberhavoc.com;uberceleb.com;udderlypettable.com','Viewmixed.com-Zonable.com-Boreburn.com-uberhavoc.com-uberceleb.com-udderlypettable.com')\
                .replace('"','')
        output.write(line)
        output.write('\n')
        if 'BRU' in row['campaign_name']:
            bru_output.writerow(row)


def main(argv):
    outfile = ''
    brufile = ''
    startdate=''
    enddate = ''
    try:
        opts, args = getopt.getopt(argv, "ho:b:s:e:", ["ofile=", "bfile=", "sdate=", "edate="])
    except getopt.GetoptError:
        print (' ERROR getting params baxReport.py -o <outfile> -b <brufile> -s <startdate> -e <enddate>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(' in opts axReport.py -o <outfile> -b <brufile> -s <startdate> -e <enddate>')
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outfile = arg
        elif opt in ("-b", "--bfile"):
            brufile = arg
        elif opt in ("-s", "--sdate"):
            startdate = arg
        elif opt in ("-e", "--edate"):
            enddate = arg

    # outfile = '/tmp/outfile.csv'
    # brufile = '/tmp/brufile.csv'
    # startdate='2016-07-31'
    # enddate = '2016-08-01'


    buildReport(startdate, enddate,outfile,brufile)

if __name__ == "__main__":
    main(sys.argv[1:])
