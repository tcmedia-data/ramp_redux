from simple_salesforce import Salesforce
import requests
import subprocess
import csv
import datetime

# Get the current date and time
now = datetime.datetime.now()
now_str = now.strftime("%Y%m%d")

sf = Salesforce(username='sgagnier@tc.tc', password='R1d1x2016', security_token='6Dm0v3MtZlrZgFF6QC6OaV4a')

cookies = dict(sid=sf.session_id)
r = requests.get("https://na4.salesforce.com/00O60000004kXAD?csv=1", cookies=cookies)

siteMapping_File= "\Users\gilbertf\Downloads\siteMapping_"+str(datetime.datetime.now().strftime('%Y%m%d'))+".csv"

with open(str(siteMapping_File), 'wb') as f:
     f.write(r.content)
     
# subprocess.Popen(siteMapping_File,shell=True)
