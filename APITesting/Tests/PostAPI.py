import requests
import json
import jsonpath

file = open("C:\\Users\\indrasen\\Downloads\\API\\PostAPI.json", "r")
v_file_text = file.read()
print(v_file_text)
print("--------------------------------------------------------------------")
print(type(v_file_text))
json_data = json.loads(v_file_text)
print("--------------------------------------------------------------------")
url = "https://reqres.in/api/users"
v_response = requests.post(url,json_data)
print(v_response.text)
print("--------------------------------------------------------------------")
print(type(v_response.text))
print("--------------------------------------------------------------------")
status_code = v_response.status_code
print(status_code)
print("--------------------------------------------------------------------")
v_json_data = json.loads(v_response.text)
print(v_json_data)
print("--------------------------------------------------------------------")
v_json_data_name = jsonpath.jsonpath(v_json_data,"name")
v_json_data_createdAt = jsonpath.jsonpath(v_json_data,"createdAt")
v_json_data_id = jsonpath.jsonpath(v_json_data,"id")
print(v_json_data_name)
print("--------------------------------------------------------------------")
print(v_json_data_createdAt)
print("--------------------------------------------------------------------")
print(v_json_data_id[0])


assert status_code == 201
