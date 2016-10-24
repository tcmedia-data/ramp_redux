# automatic_variables.py
start_date = '2016-10-20'
end_date = '2016-10-21'
suffix = start_date.replace('-','')
file_location = '/Users/tweediej/upload/'

def task_run_dfp_general_report():
    """Runs the daily dfp report"""
    return {
        'actions': ['python ./code/dfp_general_report.py  -o' + file_location + ' -s' + start_date ],
        'targets': ['DFP_General_'+ suffix + '.csv'],
    }

def task_run_appnexus_report():
    """Runs the appnexus report for the day """
    return{
        'actions': ['python3 ./code/appnexus_daily_report.py -o'+file_location +'APPNEXUS_NETWORK_'+ suffix+ '.csv -s'+start_date+' -e'+end_date],
        'targets': ['gs://managed_services/APPNEXUS_NETWORK_'+suffix +'.csv'],
    }

def task_upload_dfp_to_GCS(): 
	"""uploads the daily dfp report"""
	return {
	    'actions': ['gsutil cp ' + file_location +'DFP_General_'+ suffix + '.csv gs://managedservices_dfp'],
	    'targets': ['gs://managedservices_dfp/DFP_General_'+ suffix + '.csv'],
	}

def task_upload_appnexus_to_GCS(): 
	"""uploads the daily appnexus report"""
	return {
	    'actions': ['gsutil cp ' + file_location +'APPNEXUS_NETWORK_'+ suffix + '.csv gs://managed_service'],
	    'targets': ['APPNEXUS_NETWORK_'+ suffix + '.csv'],
	}

# def task_load_bigquery_dfp(): 
# 	"""processes the DFP table in BQ""" 
# 	return {
# 	    'actions': ['gsutil cp ' + file_location +'APPNEXUS_NETWORK_'+ suffix + '.csv gs://managed_service'],
# 	    'targets': ['APPNEXUS_NETWORK_'+ suffix + '.csv'],
# 	}
