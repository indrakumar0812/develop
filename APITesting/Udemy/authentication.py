import requests
from Udemy.utilities.config import ReadConfig

config = ReadConfig()
url= config.getAuthUrl()

#verify=False ->secure socket connection
github_response = requests.get(url,verify=False,auth=(config.getUsername(),config.getPassword()))
print(github_response.status_code)

#### To upload files

url = "https://httpbin.org/post"
file = {'file':open('report.xls','rb')}

r=requests.post(url,files=file)