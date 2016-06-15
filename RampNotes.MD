 Automation of Daily Fetch 
---

	Python Wrapper 
	1. AppNexus
	2. DFP : see DFP_General_v20160614_ok.R
	3.  SalesForce 
	  1. CRON Job


Automation Google Cloud Storage
---
	1. CRON job Daily  
	2. gcloud command line 
		2.1 gsutil -q cp C:\\Users\\gilbertf\\Desktop\\extremePixel830\\DFP\\201606\\DFP_General_20160614.csv  gs://dfp_general	
Automation Google Big Query 
---
	1. CRON job triggered by above success
	2. bq command line 
		2.1 DFP :
		bq load --replace --field_delimiter=; --skip_leading_rows=1 extreme-pixel-830:ManagedServices_DFPGeneral.DFP_General_20160614 gs://dfp_general/DFP_General_20160614.csv Date:STRING,Ad_unit:STRING,Line_item_type:STRING,Creative_size:STRING,Advertiser:STRING,Order:STRING,Salesperson:STRING,Line_item:STRING,Ad_unit_ID:INTEGER,Advertiser_ID:INTEGER,Order_ID:STRING,Salesperson_ID:INTEGER,Line_item_ID:STRING,Order_start_date:STRING,Order_end_date:STRING,Order_PO_number:STRING,Agency:STRING,Trafficker:STRING,Secondary_traffickers:STRING,Delivery_pacing:STRING,Frequency_cap:STRING,Line_item_start_date:STRING,Line_item_end_date:STRING,Cost_type:STRING,Rate_CA:STRING,Goal_quantity:STRING,Line_item_lifetime_impressions:STRING,Line_item_lifetime_clicks:STRING,Line_item_priority:STRING,Contracted_quantity:STRING,Discount:STRING,Booked_revenue_exclude_CPD_CA:STRING,Name_Comments:STRING,Audience_Segment:STRING,Total_impressions:INTEGER,Total_clicks:INTEGER,Total_CPM_and_CPC_revenue_CA:STRING,Delivery_indicator:STRING,Total_Active_View_eligible_impressions:INTEGER,Total_Active_View_viewable_impressions:INTEGER,Ad_server_CPD_revenue_CA:STRING

		2.2 APNX:
		bq load --replace --field_delimiter=; --skip_leading_rows=1 extreme-pixel-830:ManagedServices.APPNEXUS_NETWORK_20160614 gs://managed_service/APPNEXUS_NETWORK_20160614.csv processDate:STRING,publisher_id:INTEGER,publisher_name:STRING,placement_id:INTEGER,placement_name:STRING,site_id:INTEGER,site_name:STRING,size:STRING,buyer_member_id:INTEGER,buyer_member_name:STRING,seller_member_id:INTEGER,seller_member_name:STRING,advertiser_id:INTEGER,advertiser_name:STRING,line_item_id:INTEGER,line_item_name:STRING,campaign_id:INTEGER,campaign_name:STRING,bid_type:STRING,advertiser_currency:STRING,publisher_currency:STRING,imp_type:STRING,campaign_priority:STRING,media_type:STRING,line_item_type:STRING,payment_type:STRING,revenue_type:STRING,pub_rule_id:INTEGER,pub_rule_name:STRING,imps:INTEGER,clicks:INTEGER,total_convs:INTEGER,revenue:FLOAT

Write Transformation Queries [Business Rules] 
---
	1. CRON job triggered by above success
	2. bq command line : 
		2.1 DFP: see APNX_regexReplace_ManagedServicesProcessed
		2.2 APNX: see DFP_regexReplace_ManagedServicesProcessed

Write RAMP Queries
---
	1. BQL Queries in Redash 
	2. schedule refresh ferquency 

Define visualization 
---
	1. one table view 
	2. one graph [ecpm & revenue]

	- Dimensions for filtering 
	1. Publisher 
	2. Time 
	3. Media Type 
	4. Network 
	5. Currency 
	6. Size **New 

Apply Security and Filters 
---
	1. dashboard per publisher 
	2. filter per query template 

Google DNS Config 
---


