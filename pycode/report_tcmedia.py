from googleads import dfp
from googleads import errors
import datetime
import tempfile


def getReport():
    client = dfp.DfpClient.LoadFromStorage()
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
                           # ,'AUDIENCE_SEGMENT_NAME' #ReportError.COLUMNS_NOT_SUPPORTED_FOR_REQUESTED_DIMENSIONS @ columns; trigger:'ADSENSE_ACTIVE_VIEW_ELIGIBLE_IMPRESSIONS, ADSENSE_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS, ADSENSE_LINE_ITEM_LEVEL_CLICKS, ADSENSE_LINE_ITEM_LEVEL_IMPRESSIONS, ADSENSE_LINE_ITEM_LEVEL_REVENUE, AD_EXCHANGE_ACTIVE_VIEW_ELIGIBLE_IMPRESSIONS, AD_EXCHANGE_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS, AD_EXCHANGE_LINE_ITEM_LEVEL_CLICKS, AD_EXCHANGE_LINE_ITEM_LEVEL_IMPRESSIONS, AD_EXCHANGE_LINE_ITEM_LEVEL_REVENUE, AD_SERVER_ACTIVE_VIEW_ELIGIBLE_IMPRESSIONS, AD_SERVER_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS, AD_SERVER_CLICKS, AD_SERVER_CPD_REVENUE, AD_SERVER_CPM_AND_CPC_REVENUE, AD_SERVER_IMPRESSIONS, TOTAL_LINE_ITEM_LEVEL_ALL_REVENUE, TOTAL_LINE_ITEM_LEVEL_CLICKS, TOTAL_LINE_ITEM_LEVEL_IMPRESSIONS']'
                , 'PROPOSAL_AGENCY_NAME'
                , 'PROPOSAL_AGENCY_ID'

                           # , 'PRODUCT_ID'
                # , 'PROPOSAL_ID'

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

                 # , 'PROPOSAL_LINE_ITEM_COMMENTS'
                 # , 'LINE_ITEM_TYPE_PRODUCT'
                 ]
            # ,'statement': filter_statement
            ##--------------------------
            , 'adUnitView': 'HIERARCHICAL'  # 'FLAT'
            # COLS HERE: https://developers.google.com/doubleclick-publishers/docs/reference/v201608/ReportService.Column

            , 'columns': [
                'TOTAL_LINE_ITEM_LEVEL_IMPRESSIONS'
                , 'TOTAL_LINE_ITEM_LEVEL_CLICKS'
                , 'TOTAL_LINE_ITEM_LEVEL_ALL_REVENUE'
                 # , 'AD_SERVER_DELIVERY_INDICATOR'
                #LINE ABOVE CHANGED TO LINE BELOW WITH API VERSION v201608
                # , 'LINE_ITEM_DELIVERY_INDICATOR'
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
            , 'dateRangeType': 'YESTERDAY'

        }

    }
    # Initialize a DataDownloader.
    report_downloader = client.GetDataDownloader(version='v201605')
    # report_service
    try:
        # Run the report and wait for it to finish.
        report_job_id = report_downloader.WaitForReport(report_job)
    except errors.DfpReportError, e:
        print 'Failed to generate report. Error was: %s' % e

    # Change to your preferred export format.
    export_format = 'CSV_DUMP'

    report_file = tempfile.NamedTemporaryFile(suffix='.csv.gz', delete=False)

    # Download report data.
    report_downloader.DownloadReportToFile(report_job_id, export_format, report_file)

    report_file.close()

    # Display results.
    print 'Report job with id \'%s\' downloaded to:\n%s' % (
        report_job_id, report_file.name)


getReport()
