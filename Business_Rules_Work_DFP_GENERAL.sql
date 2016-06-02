SELECT
[Date],
[Ad_unit],
[Line_item_type],
[Creative_size],
[Advertiser],
[Order],
[Salesperson],
[Line_item],
[Ad_unit_ID],
[Advertiser_ID],
[Order_ID],
[Salesperson_ID],
[Line_item_ID],
[Order_start_date],
[Order_end_date],
[Order_PO_number],
[Agency],
[Trafficker],
[Secondary_traffickers],
[Delivery_pacing],
[Frequency_cap],
[Line_item_start_date],
[Line_item_end_date],
[Cost_type],
[Rate_CA],
[Goal_quantity],
[Line_item_lifetime_impressions],
[Line_item_lifetime_clicks],
[Line_item_priority],
[Contracted_quantity],
[Discount],
[Booked_revenue_exclude_CPD_CA],
[Name_Comments],
[Audience_Segment],
[Total_impressions],
[Total_clicks],
[Total_CPM_and_CPC_revenue_CA],
[Delivery_indicator],
[Total_Active_View_eligible_impressions],
[Total_Active_View_viewable_impressions],
[Ad_server_CPD_revenue_CA],

//---------------------------------------------
//New column [PlatformID]
CASE WHEN [Advertiser] = 'appnexus - remnant' THEN 2
WHEN [Advertiser] = 'google - remnant' THEN 3
WHEN [Advertiser] = 'liverail' THEN 4
WHEN [Advertiser] = 'rubicon - remnant' THEN 5
WHEN [Advertiser] = 'lkqd' THEN 6
WHEN [Advertiser] = 'sm [dfp]' THEN 7
ELSE 1 END AS [PlatformID],  

//[axLineItemTypeID]
99 AS [axLineItemTypeID],

//[axImpTypeID]
99 AS [axImpTypeID],

//[axMediaTypeID]
99 AS [axMediaTypeID],

//---------------------------------------------
//[CamTypeID]
CASE WHEN [Line_item] like '%- ron %' THEN  3
WHEN [Line_item] like '%- roc %' THEN  2
WHEN [Line_item] like '%- ros %' THEN  1
WHEN [Line_item] like '%sponsorship%' THEN  1
WHEN [Line_item] like '%house%' THEN  1
WHEN [Line_item] like '%targeting%' THEN  3
WHEN [Order] like '%appnexus%' OR [Order] like '%google%' OR [Order] like '%rubicon%' THEN  3
WHEN [Order] like '%house%' THEN  1
ELSE 99 END AS [CamTypeID],

//---------------------------------------------
//New column [RevTypeID]
99 AS [RevTypeID],

//---------------------------------------------
//New column [ManagedID]
99 AS [ManagedID],

//---------------------------------------------
//New column [AdTypeID]
99 AS [AdTypeID],

//---------------------------------------------
//New column [TechFee] = $0.01357 based on Network Total Impressions count / each participant
0 AS [TechFee]

FROM [Business_Rules_Work.DFP_General_20160501]

IGNORE CASE //required for string lookups





