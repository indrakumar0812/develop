import json

import jsonpath
import requests

test_url = "https://reqres.in/api/users?page=2"
v_response = requests.get(test_url)
v_data = v_response.text
print(type(v_data))
v_statuscode = v_response.status_code
print(v_statuscode)
v_json = json.loads(v_data)
v_per_page = jsonpath.jsonpath(v_json,"per_page")
v_data_elements = jsonpath.jsonpath(v_json,"data")
#print(v_data_elements)
print(v_per_page[0])
print(len(v_data_elements[0]))

assert v_statuscode == 200
#assert v_per_page[0] == len(v_data_elements[0])
