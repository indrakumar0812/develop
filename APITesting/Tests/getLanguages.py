import requests
import json
import jsonpath

country="India"
baseurl = "https://restcountries.eu/rest/v2/name/"
resource = "India"
endpoint = baseurl+resource

response = requests.get(endpoint,params={'fullText':'true'})
print(response.status_code)
json_data=response.json()
print(type(json_data))


lang = jsonpath.jsonpath(json_data[0],'languages')
print(lang[0][1]['name'])
#print(json_data[0]['languages'][0]['name'])