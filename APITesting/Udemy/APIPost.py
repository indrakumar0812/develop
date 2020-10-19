import requests
import json
from Udemy.payload import *
from Udemy.utilities.config import ReadConfig
from Udemy.resources import *


headers = {"Content-Type":"application/json"}

baseUrl = ReadConfig.getUrl() + Apiresources.addUser

resp_data = requests.post(baseUrl,json=getPayload(),headers=headers)

print(resp_data.status_code)
res_data = resp_data.json()
print(res_data['id'])
