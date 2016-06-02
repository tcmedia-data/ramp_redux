SELECT
[processDate],
[publisher_id],
[publisher_name],
[placement_id],
[placement_name],
[site_id],
[site_name],
[size],
[buyer_member_id],
[buyer_member_name],
[seller_member_id],
[seller_member_name],
[advertiser_id],
[advertiser_name],
[line_item_id],
[line_item_name],
[campaign_id],
[campaign_name],
[bid_type],
[advertiser_currency],
[publisher_currency],
[imp_type],
[campaign_priority],
[media_type],
[line_item_type],
[payment_type],
[revenue_type],
[pub_rule_id],
[pub_rule_name],
[imps],
[clicks],
[total_convs],
[revenue],

//Platform_ID_APPNEXUS
2 AS [PlatformID], 

//axLineItemTypeID
CASE WHEN [line_item_type]= '--' THEN 0 
WHEN [line_item_type]= 'ssp' THEN 1 
WHEN [line_item_type]= 'remnant' THEN 2
WHEN [line_item_type]= 'managed' THEN 3
WHEN [line_item_type]= 'test' THEN 98
ELSE 99
END AS axLineItemTypeID,

//axImpTypeID
CASE WHEN [imp_type] = 'blank' THEN 0
WHEN [imp_type] = 'default' THEN 1
WHEN [imp_type] = 'kept' THEN 2
WHEN [imp_type] = 'psa' THEN 3
WHEN [imp_type] = 'resold' THEN 4
WHEN [imp_type] = 'rtb' THEN 5
ELSE 99
END AS [axImpTypeID],

//axMediaType
CASE WHEN [media_type] = '--' THEN 0
WHEN [media_type] = 'banner' THEN 1
WHEN [media_type] = 'expandable' THEN 2
WHEN [media_type] = 'high impact' THEN 3
WHEN [media_type] = 'video' THEN 4
WHEN [media_type] = 'text' THEN 5
ELSE 99
END AS [axMediaTypeID],

//---------------------------------------------
//New column [CamTypeID]
CASE WHEN [media_type] = 'video' THEN 3 //'ron'
WHEN [line_item_type] = 'remnant' OR [payment_type] like '%revshare%' THEN 3 //'ron' 
WHEN [line_item_type] = 'ssp'OR [line_item_name] like '%twig%' THEN 3 //'ron' 
WHEN [imp_type] = 'psa' OR [imp_type] = 'default' THEN 3 //'ron'   
WHEN [imp_type] = 'resold' THEN 3 //'ron'      
ELSE 3 END AS [CamTypeID], //Placeholder Code in case future usage of ROC in APNX

//---------------------------------------------
//New column [RevTypeID]
CASE WHEN [media_type] = 'video' THEN 1 //'managed'  
WHEN [line_item_type] = 'remnant' OR [payment_type] like '%revshare%' THEN 1 //'managed'  
WHEN [line_item_type] = 'ssp' OR [line_item_name] like '%twig%' THEN 1 //'managed' 
WHEN [imp_type] = 'psa' OR [imp_type] = 'default' THEN 1 //'managed' 
WHEN [imp_type] = 'resold' THEN  2 //'linked'
ELSE 3 END AS [RevTypeID],

//---------------------------------------------
//New column [ManagedID]
CASE WHEN [media_type] = 'video' THEN 0 //'unknown'  
WHEN [line_item_type] = 'remnant' OR [payment_type] like '%revshare%' THEN 3 //'unknown' 
WHEN [line_item_type] = 'ssp' OR [line_item_name] like '%twig%' THEN 2 //'ssp' 
WHEN [imp_type] = 'psa' OR [imp_type] = 'default' THEN 4 //'house'  
WHEN [imp_type] = 'resold' THEN 0 //'unknown'   
ELSE 1 END AS [ManagedID],

//---------------------------------------------
//New column [AdTypeID]
CASE WHEN [media_type] = 'video' THEN 2 //'video'
WHEN [line_item_type] = 'remnant' OR [payment_type] like '%revshare%' THEN 1 //'display' 
WHEN [line_item_type] = 'ssp' OR [line_item_name] like '%twig%' THEN 1 //'display' 
WHEN [imp_type] = 'psa' OR [imp_type] = 'default' THEN 1 //'display'
WHEN [imp_type] = 'resold' THEN 1 //'display'  
ELSE 1 END AS [AdTypeID],

//---------------------------------------------
//New column [TechFee] = $0.015 CPM WHERE [ImpType] = Blank, PSA, Default Error, Default, Kept, & PSA Error.
CASE WHEN [imp_type] = 'rtb' OR [imp_type] ='psa' THEN 0
ELSE 0.015 END AS [TechFee],

FROM [Business_Rules_Work.APPNEXUS_20160501]
//FROM [Business_Rules_Work.APNX_testCASE_20160501]
WHERE[publisher_name] LIKE '%FanOWeb%'

IGNORE CASE

