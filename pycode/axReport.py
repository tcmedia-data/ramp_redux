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

    filters = [{"imps":{"operator":"!=","value": 6}}]

    report = AppnexusReport(start_date=startDate,
                            end_date=endDate,
                            #filters=filters,
                            report_type=report_type,
                            columns=columns)

    output_json = report.get()

    output = csv.DictWriter(open(outfile , 'w'), fieldnames=columns, delimiter=';')
    bru_output = csv.DictWriter(open(bruFile, 'w'), fieldnames=columns, delimiter=';')
    output.writeheader()
    for row in output_json:
        output.writerow(row)
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

    buildReport(startdate, enddate,outfile,brufile)

if __name__ == "__main__":
    main(sys.argv[1:])
