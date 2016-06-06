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
CAST([imps] AS INTEGER) AS imps,
CAST([clicks] AS INTEGER) AS clicks,
CAST([total_convs]  AS INTEGER) AS total_convs,
CAST([revenue] AS FLOAT) AS revenue,

//---------------------------------------------
//Platform_ID_APPNEXUS
'APPNexus' AS [PlatformNAME], 
2 AS [PlatformID], 

//---------------------------------------------
//axLineItemTypeNAME
CASE WHEN [line_item_type]= '--' THEN '--' 
WHEN [line_item_type]= 'ssp' THEN 'SSP'
WHEN [line_item_type]= 'remnant' THEN 'Remnant'
WHEN [line_item_type]= 'managed' THEN 'Managed'
WHEN [line_item_type]= 'test' THEN 'Test'
ELSE 'Unknown'
END AS axLineItemTypeNAME,

//axLineItemTypeID
CASE WHEN [line_item_type]= '--' THEN 0 
WHEN [line_item_type]= 'ssp' THEN 1 
WHEN [line_item_type]= 'remnant' THEN 2
WHEN [line_item_type]= 'managed' THEN 3
WHEN [line_item_type]= 'test' THEN 98
ELSE 99
END AS axLineItemTypeID,

//---------------------------------------------
//axImpTypeNAME
CASE WHEN [imp_type] = 'blank' THEN 'Blank'
WHEN [imp_type] = 'default' THEN 'Default'
WHEN [imp_type] = 'kept' THEN 'Kept'
WHEN [imp_type] = 'psa' THEN 'PSA'
WHEN [imp_type] = 'resold' THEN 'Resold'
WHEN [imp_type] = 'rtb' THEN 'RTB'
ELSE 'Unknown'
END AS [axImpTypeNAME],

//axImpTypeID
CASE WHEN [imp_type] = 'blank' THEN 0
WHEN [imp_type] = 'default' THEN 1
WHEN [imp_type] = 'kept' THEN 2
WHEN [imp_type] = 'psa' THEN 3
WHEN [imp_type] = 'resold' THEN 4
WHEN [imp_type] = 'rtb' THEN 5
ELSE 99
END AS [axImpTypeID],

//---------------------------------------------
//axMediaTypeNAME
CASE WHEN [media_type] = '--' THEN '--'
WHEN [media_type] = 'banner' THEN 'Banner'
WHEN [media_type] = 'expandable' THEN 'Expandable'
WHEN [media_type] = 'high impact' THEN 'High Impact'
WHEN [media_type] = 'video' THEN 'Video'
WHEN [media_type] = 'text' THEN 'Text'
ELSE 'Unknown'
END AS [axMediaTypeNAME],

//axMediaTypeID
CASE WHEN [media_type] = '--' THEN 0
WHEN [media_type] = 'banner' THEN 1
WHEN [media_type] = 'expandable' THEN 2
WHEN [media_type] = 'high impact' THEN 3
WHEN [media_type] = 'video' THEN 4
WHEN [media_type] = 'text' THEN 5
ELSE 99
END AS [axMediaTypeID],

//---------------------------------------------

//New column [CamTypeNAME] 
//NOTE: Placeholder Code in case future usage of ROC in APNX
CASE WHEN [media_type] = 'video' THEN 'RON'
WHEN [line_item_type] = 'remnant' OR [payment_type] like '%revshare%' THEN 'RON' 
WHEN [line_item_type] = 'ssp'OR [line_item_name] like '%twig%' THEN 'RON'
WHEN [imp_type] = 'psa' OR [imp_type] = 'default' THEN 'RON'  
WHEN [imp_type] = 'resold' THEN 'RON'     
ELSE 'RON' END AS [CamTypeNAME], 

//New column [CamTypeID]
CASE WHEN [media_type] = 'video' THEN 3
WHEN [line_item_type] = 'remnant' OR [payment_type] like '%revshare%' THEN 3
WHEN [line_item_type] = 'ssp'OR [line_item_name] like '%twig%' THEN 3
WHEN [imp_type] = 'psa' OR [imp_type] = 'default' THEN 3  
WHEN [imp_type] = 'resold' THEN 3     
ELSE 3 END AS [CamTypeID], 

//---------------------------------------------
//New column [RevTypeNAME]
CASE WHEN [media_type] = 'video' THEN 'Managed'  
WHEN [line_item_type] = 'remnant' OR [payment_type] like '%revshare%' THEN 'Managed'  
WHEN [line_item_type] = 'ssp' OR [line_item_name] like '%twig%' THEN 'Managed'
WHEN [imp_type] = 'psa' OR [imp_type] = 'default' THEN 'Managed'
WHEN [imp_type] = 'resold' THEN  'Linked'
ELSE 'SSP' END AS [RevTypeNAME],

//New column [RevTypeID]
CASE WHEN [media_type] = 'video' THEN 1  
WHEN [line_item_type] = 'remnant' OR [payment_type] like '%revshare%' THEN 1  
WHEN [line_item_type] = 'ssp' OR [line_item_name] like '%twig%' THEN 1 
WHEN [imp_type] = 'psa' OR [imp_type] = 'default' THEN 1
WHEN [imp_type] = 'resold' THEN  2
ELSE 3 END AS [RevTypeID],

//---------------------------------------------
//New column [ManagedNAME]
//CASE WHEN [media_type] = 'video' THEN 'Unknown'  
//WHEN [line_item_type] = 'remnant' OR [payment_type] like '%revshare%' THEN 'Remnant'
//WHEN [line_item_type] = 'ssp' OR [line_item_name] like '%twig%' THEN 'SSP'
//WHEN [imp_type] = 'psa' OR [imp_type] = 'default' THEN 'House'  
//WHEN [imp_type] = 'resold' THEN 'Unknown'   
//ELSE 'Direct' END AS [ManagedNAME],

//New column [ManagedID]
CASE WHEN [media_type] = 'video' THEN 99 
WHEN [line_item_type] = 'remnant' OR [payment_type] like '%revshare%' THEN 3 
WHEN [line_item_type] = 'ssp' OR [line_item_name] like '%twig%' THEN 2
WHEN [imp_type] = 'psa' OR [imp_type] = 'default' THEN 4  
WHEN [imp_type] = 'resold' THEN 99   
ELSE 1 END AS [ManagedID],

//---------------------------------------------
//New column [AdTypeNAME]
CASE WHEN [media_type] = 'video' THEN 'Video'
WHEN [line_item_type] = 'remnant' OR [payment_type] like '%revshare%' THEN 'Display' 
WHEN [line_item_type] = 'ssp' OR [line_item_name] like '%twig%' THEN 'Display' 
WHEN [imp_type] = 'psa' OR [imp_type] = 'default' THEN 'Display'
WHEN [imp_type] = 'resold' THEN 'Display'  
ELSE 'Display' END AS [AdTypeNAME],

//New column [AdTypeID]
CASE WHEN [media_type] = 'video' THEN 2
WHEN [line_item_type] = 'remnant' OR [payment_type] like '%revshare%' THEN 1 
WHEN [line_item_type] = 'ssp' OR [line_item_name] like '%twig%' THEN 1
WHEN [imp_type] = 'psa' OR [imp_type] = 'default' THEN 1
WHEN [imp_type] = 'resold' THEN 1  
ELSE 1 END AS [AdTypeID],

//---------------------------------------------
//New column [TechFee] = $0.015 CPM WHERE [ImpType] = Blank, PSA, Default Error, Default, Kept, & PSA Error.
CASE WHEN [imp_type] = 'rtb' OR [imp_type] ='psa' THEN 0
ELSE 0.015 END AS [TechFee],

FROM [Business_Rules_Work.APPNEXUS_20160501]
WHERE[publisher_name] LIKE '%FanOWeb%' AND 
[DATE] <> 'Total'

IGNORE CASE
