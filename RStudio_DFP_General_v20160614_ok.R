#https://github.com/ReportMort/rdfp
#devtools::install_github("ReportMort/rdfp")
library("rdfp")

#check for working directory 
#HOME wrkdir='C:\\Users\\frederic\\SkyDrive\\WORK\\R'
wrkdir="C:\\Users\\gilbertf\\Desktop\\extremePixel830"
if (getwd()!=wrkdir) {
  setwd(wrkdir)
}

#https://console.developers.google.com/apis/credentials?project=extreme-pixel-830 OK
options(rdfp.network_code = "4916")
options(rdfp.application_name = "rstudio")
options(rdfp.client_id = "592844875481-fpvtvdq07ih7hnead42c05nmeu6jk0fd.apps.googleusercontent.com")
options(rdfp.client_secret = "QPBMa9jVYDjoAa0LljdU0QV3")
dfp_auth()

#Change dateValue 
dateValue ="14"
monthValue = "06"
yearValue = "2016"

#levelAd = 'TOP_LEVEL'
#levelAd = 'FLAT'
levelAd = 'HIERARCHICAL'

outputDFP = "DFP_General_v8.csv"

# create a reportJob object
# reportJobs consist of a reportQuery
# Documentation for the reportQuery object can be found in R using 
# ?dfp_ReportService_object_factory and searching for ReportQuery
# Also online documentation is available that lists available child elements for reportQuery

# https://developers.google.com/doubleclick-publishers/docs/reference/v201508/ReportService.ReportQuery#dimensionattributes
request_data <- list(reportJob=list(reportQuery=list(
  #dimensions='DATE',
  dimensions='AD_UNIT_NAME',
  dimensions='LINE_ITEM_TYPE',
  dimensions='CREATIVE_SIZE',
  dimensions='ADVERTISER_NAME',
  
  #problem with ORDER_NAME when  
  #dimensions='ORDER_NAME',
  
  dimensions='SALESPERSON_NAME',
  dimensions='LINE_ITEM_NAME',
  dimensions='AD_UNIT_ID',
  dimensions='ADVERTISER_ID',
  dimensions='ORDER_ID',
  dimensions='SALESPERSON_ID',
  dimensions='LINE_ITEM_ID',
  dimensions='ORDER_START_DATE_TIME',
  dimensions='ORDER_END_DATE_TIME',
  dimensions='ORDER_PO_NUMBER',
  dimensions='ORDER_AGENCY',
  dimensions='ORDER_TRAFFICKER',
  dimensions='ORDER_SECONDARY_TRAFFICKERS',
  dimensions='LINE_ITEM_DELIVERY_PACING',
  dimensions='LINE_ITEM_FREQUENCY_CAP',
  dimensions='LINE_ITEM_START_DATE',
  dimensions='LINE_ITEM_END_DATE',
  dimensions='LINE_ITEM_COST_TYPE',
  dimensions='PROPOSAL_LINE_ITEM_TARGET_RATE_NET',
  dimensions='LINE_ITEM_GOAL_QUANTITY',
  dimensions='LINE_ITEM_LIFETIME_IMPRESSIONS',
  dimensions='LINE_ITEM_LIFETIME_CLICKS',
  dimensions='LINE_ITEM_PRIORITY',
  dimensions='LINE_ITEM_CONTRACTED_QUANTITY',
  dimensions='LINE_ITEM_DISCOUNT',
  dimensions='LINE_ITEM_NON_CPD_BOOKED_REVENUE',
  dimensions='PROPOSAL_LINE_ITEM_COMMENTS',
  dimensions='AUDIENCE_SEGMENT_NAME',
  dimensions='AD_SERVER_DELIVERY_INDICATOR',
  
  adUnitView=levelAd,
  
  columns='AD_SERVER_IMPRESSIONS', 
  columns='AD_SERVER_CLICKS', 
  columns='AD_SERVER_CPM_AND_CPC_REVENUE',
  
  columns='TOTAL_ACTIVE_VIEW_ELIGIBLE_IMPRESSIONS',
  columns='TOTAL_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS',
  columns='AD_SERVER_CPD_REVENUE',
  
  startDate=list(year=yearValue, month=monthValue, day=dateValue),
  endDate=list(year=yearValue, month=monthValue, day=dateValue),
  dateRangeType='CUSTOM_DATE'
)))

# a convenience function has been provided to you to manage the report process workflow
# if you would like more control, see the example below which moves through each step in the process
#report_data <- dfp_full_report_wrapper(request_data)

#---------------------
# REMOVE LAST 2 COLUMNS
head(report_data)
#names(report_data)
#report.data[14:15] <- NULL

#Rename Cols Headers to comply with BQ no dot in headers policy NOT WORKING MORE TEST REQUIRED
#no order _name
#names(report_data) <- c("DATE","AD_UNIT_NAME","AD_UNIT_ID","AD_SERVER_IMPRESSIONS","AD_SERVER_CLICKS","AD_SERVER_CPM_AND_CPC_REVENUE","TOTAL_ACTIVE_VIEW_ELIGIBLE_IMPRESSIONS","TOTAL_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS","AD_SERVER_CPD_REVENUE")

#https://stat.ethz.ch/R-manual/R-devel/library/utils/html/write.table.html
write.csv2(report_data, file=outputDFP ,row.names=FALSE,quote=FALSE)


