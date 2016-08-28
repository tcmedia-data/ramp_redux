from nexusadspy import AppnexusReport
import json
import csv
import sys, getopt


def formatGoogleDate(axDate):
    #axDate
    #'2016-07-31'
    #google date
    #07/26/2016
    return '/'.join([axDate.split('-')[1],axDate.split('-')[2],axDate.split('-')[0]]).replace('"','')

def cleanPublisherName(publisher_name):
    return publisher_name.replace(';','-').replace(',','-')

def buildReport(startDate, endDate, outfile):
    columns = ["day",
               "publisher_id",
               "publisher_name",
               "placement_id",
               "placement_name",
               "site_id",
               "site_name",
               "size",
               "buyer_member_id",
               "buyer_member_name",
               "seller_member_id",
               "seller_member_name",
               "advertiser_id",
               "advertiser_name",
               "line_item_id",
               "line_item_name",
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
               "pub_rule_id",
               "pub_rule_name",
               "imps",
               "clicks",
               "total_convs",
               "revenue"]

    report_type = "network_analytics"
    SEMI = ';'

    report = AppnexusReport(start_date=startDate,
                            end_date=endDate,
                            report_type=report_type,
                            columns=columns,
                            timezone='UTC')
    output_json = report.get()
    output = open(outfile , 'w', newline='')
    output.write (';'.join(columns) + '\n')
    for row in output_json:
        row['"publisher_name"'] = cleanPublisherName(row['"publisher_name"'])
        line = formatGoogleDate(row['"day"'])\
               + SEMI + row['"publisher_id"']\
               + SEMI + row['"publisher_name"'] \
               + SEMI + row['"placement_id"']\
               + SEMI + row['"placement_name"']\
               + SEMI + row['"site_id"']\
               + SEMI + row['"site_name"'] \
               + SEMI + row['"size"'] \
               + SEMI + row['"buyer_member_id"']\
               + SEMI + row['"buyer_member_name"']\
               + SEMI + row['"seller_member_id"']\
               + SEMI + row['"seller_member_name"']\
               + SEMI + row['"advertiser_id"']\
               + SEMI + row['"advertiser_name"']\
               + SEMI + row['"line_item_id"']\
               + SEMI + row['"line_item_name"']\
               + SEMI + row['"campaign_id"']\
               + SEMI + row['"campaign_name"']\
               + SEMI + row['"bid_type"'] \
               + SEMI + row['"advertiser_currency"'] \
               + SEMI + row['"publisher_currency"']\
               + SEMI + row['"imp_type"']\
               + SEMI + row['"campaign_priority"']\
               + SEMI + row['"media_type"']\
               + SEMI + row['"line_item_type"']\
               + SEMI + row['"payment_type"']\
               + SEMI + row['"revenue_type"'] \
               + SEMI + row['"pub_rule_id"']\
               + SEMI + row['"pub_rule_name"']\
               + SEMI + row['"imps"']\
               + SEMI + row['"clicks"']\
               + SEMI + row['"total_convs"']\
               + SEMI + row['"revenue"']

        output.write(line.replace('"',''))
        output.write('\n')
        output.flush()

def main(argv):
    outfile = ''
    startdate=''
    enddate = ''
    try:
        opts, args = getopt.getopt(argv, "ho:s:e:", ["ofile=",  "sdate=", "edate="])
    except getopt.GetoptError:
        print (' ERROR getting params axReport.py -o <outfile>  -s <startdate> -e <enddate>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(' in opts axReport.py -o <outfile>  -s <startdate> -e <enddate>')
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outfile = arg
        elif opt in ("-s", "--sdate"):
            startdate = arg
        elif opt in ("-e", "--edate"):
            enddate = arg

    outfile = '/Users/tweediej/upload/APPNEXUS_NETWORK_20160731.csv'
    startdate='2016-07-31'
    enddate = '2016-08-01'


    buildReport(startdate, enddate,outfile)

if __name__ == "__main__":
    main(sys.argv[1:])
