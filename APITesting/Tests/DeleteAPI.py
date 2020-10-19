import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

v_response = requests.delete(url)
status_code = v_response.status_code
print(status_code)
content = v_response.text
print(len(content))
size = len(content)

assert status_code == 204
assert size == 0