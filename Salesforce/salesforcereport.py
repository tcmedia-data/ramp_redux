from simple_salesforce import Salesforce
import requests
import subprocess

sf = Salesforce(username='sgagnier@tc.tc', password='R1d1x2016', security_token='6Dm0v3MtZlrZgFF6QC6OaV4a')

cookies = dict(sid=sf.session_id)
r = requests.get("https://na4.salesforce.com/00O60000004kXAD?csv=1", cookies=cookies)
with open('\Users\gilbertf\Downloads\SiteMapping_NEW.csv', 'w') as f:
     f.write(r.content)
subprocess.Popen('\Users\gilbertf\Downloads\SiteMapping_NEW.csv',shell=True)
