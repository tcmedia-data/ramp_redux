from googleads import dfp
from googleads import errors
import datetime
import tempfile
import sys, getopt
import gzip 


def getReport(startdate ,outfile):
    client = dfp.DfpClient.LoadFromStorage()
    start_date = datetime.datetime.strptime(startdate,'%Y-%m-%d')
    end_date = start_date

    # Create report job.
    report_job = {
        'reportQuery': {
            'dimensions': ['DATE'
                , 'AD_UNIT_NAME'
                , 'LINE_ITEM_TYPE'
                , 'CREATIVE_SIZE'
                , 'ADVERTISER_NAME'
                , 'ORDER_NAME'
                , 'SALESPERSON_NAME'
                , 'LINE_ITEM_NAME'
                , 'PRODUCT_TEMPLATE_NAME'
                , 'MASTER_COMPANION_CREATIVE_NAME'
                , 'AD_UNIT_ID'
                , 'ADVERTISER_ID'
                , 'ORDER_ID'
                , 'SALESPERSON_ID'
                , 'LINE_ITEM_ID'
                , 'PRODUCT_TEMPLATE_ID'
                , 'MASTER_COMPANION_CREATIVE_ID'
                , 'PROPOSAL_AGENCY_NAME'
                , 'PROPOSAL_AGENCY_ID'
                           ],
            'dimensionAttributes':
                ['ORDER_START_DATE_TIME'
                    , 'ORDER_END_DATE_TIME'
                    , 'ORDER_PO_NUMBER'
                    , 'ORDER_TRAFFICKER'
                    , 'ORDER_SECONDARY_TRAFFICKERS'
                    , 'LINE_ITEM_DELIVERY_PACING'
                    , 'LINE_ITEM_FREQUENCY_CAP'
                    , 'LINE_ITEM_START_DATE_TIME'
                    , 'LINE_ITEM_END_DATE_TIME'
                    , 'LINE_ITEM_COST_TYPE'
                    , 'LINE_ITEM_GOAL_QUANTITY'
                    , 'LINE_ITEM_LIFETIME_IMPRESSIONS'
                    , 'LINE_ITEM_LIFETIME_CLICKS'
                    , 'LINE_ITEM_PRIORITY'
                    , 'LINE_ITEM_CONTRACTED_QUANTITY'
                    , 'LINE_ITEM_DISCOUNT'
                    , 'MASTER_COMPANION_TYPE'
                    , 'LINE_ITEM_COST_PER_UNIT'
                ]
            , 'adUnitView': 'HIERARCHICAL'  

            , 'columns': [
                'TOTAL_LINE_ITEM_LEVEL_IMPRESSIONS'
                , 'TOTAL_LINE_ITEM_LEVEL_CLICKS'
                , 'TOTAL_LINE_ITEM_LEVEL_ALL_REVENUE'
                , 'AD_SERVER_IMPRESSIONS'
                , 'AD_SERVER_CLICKS'
                , 'AD_SERVER_CPM_AND_CPC_REVENUE'
                , 'AD_SERVER_CPD_REVENUE'
                , 'AD_SERVER_ACTIVE_VIEW_ELIGIBLE_IMPRESSIONS'
                , 'AD_SERVER_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS'
                , 'ADSENSE_LINE_ITEM_LEVEL_IMPRESSIONS'
                , 'ADSENSE_LINE_ITEM_LEVEL_CLICKS'
                , 'ADSENSE_LINE_ITEM_LEVEL_REVENUE'
                , 'ADSENSE_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS'
                , 'ADSENSE_ACTIVE_VIEW_ELIGIBLE_IMPRESSIONS'
                , 'AD_EXCHANGE_LINE_ITEM_LEVEL_IMPRESSIONS'
                , 'AD_EXCHANGE_LINE_ITEM_LEVEL_CLICKS'
                , 'AD_EXCHANGE_LINE_ITEM_LEVEL_REVENUE'
                , 'AD_EXCHANGE_ACTIVE_VIEW_ELIGIBLE_IMPRESSIONS'
                , 'AD_EXCHANGE_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS'
            ]
            ,'dateRangeType': 'CUSTOM_DATE',
                'startDate': {'year': start_date.year,
                              'month': start_date.month,
                              'day': start_date.day},
                  'endDate': {'year': end_date.year,
                              'month': end_date.month,
                              'day': end_date.day}

        }

    }
    # Initialize a DataDownloader.
    # report_downloader = client.GetDataDownloader(version='v201605') # OLD 2016
    
    report_downloader = client.GetDataDownloader(version='v201805') 
    # FG 20180604 FROM https://developers.google.com/doubleclick-publishers/docs/deprecation
    
    try:
        print ('starting job for ' + str(start_date.date()))
        # Run the report and wait for it to finish.
        report_job_id = report_downloader.WaitForReport(report_job)
    except errors.DfpReportError:
        print ('Failed to generate report. Error was: %s' % errors.DfpReportError.message)

    # Change to your preferred export format.
    export_format = 'CSV_DUMP'

    report_file = tempfile.NamedTemporaryFile(prefix='DFP_General_' + str(startdate), suffix='.csv.gz', delete=False)

    # Download report data.
    report_downloader.DownloadReportToFile(report_job_id, export_format, report_file)
    output_file = outfile + 'DFP_General_' + str(startdate).replace('-','') + '.csv'
    report_file.close()
    unzipit(report_file.name, output_file)
    print ('Report job with id \'%s\' downloaded to:\n%s' % (
        report_job_id, report_file.name))
    # give doit something
    return output_file


    
    

def unzipit(report_file, output_file):
    with gzip.open(report_file,'rb') as inputfile:
        with open(output_file, 'wb') as outfile:
            for line in inputfile:
                outfile.write(line)
    print 'Report job with id \'%s\' unzipped to:\n%s' % (report_file, output_file)


def main(argv):
    outfile = ''
    startdate = ''
    enddate = ''
    try:
        opts, args = getopt.getopt(argv, "ho:s:e:", ["ofile=", "sdate="])
    except getopt.GetoptError:
        print(' ERROR getting params dfp_general_report.py -o <DFP_Generalyyyymmdd.csv>  -s <yyyy-mm-dd>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(' in opts dfp_general_report.py -o <outfile>  -s <startdate>')
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outfile = arg
        elif opt in ("-s", "--sdate"):
            startdate = arg

    filename = getReport(startdate, outfile)
    print(filename)

if __name__ == "__main__":
    main(sys.argv[1:])
