import requests
import json
import jsonpath

file = open("C:\\Users\\indrasen\\Downloads\\API\\PostAPI.json","r")
v_text = file.read()
print(v_text)
v_input_data = json.loads(v_text)

print("-----------------------------------")
v_input_name = v_input_data['name']
print(v_input_name)
print("-----------------------------------")

v_input_job = v_input_data['job']
print(v_input_job)
print("-----------------------------------")

#print(type(v_json_data))-->Dict
url="https://reqres.in/api/users/2"

v_response = requests.put(url,v_input_data)
print("-----------------------------------")
print(v_response.text)
status_code = v_response.status_code
print("-----------------------------------")
print(status_code)
v_jsonData = json.loads(v_response.text)

print("-----------------------------------")
print(v_jsonData)
#print(type(v_jsonData))-->Dict


print("------------ v_name -----------------------")
v_name = jsonpath.jsonpath(v_jsonData,"name")
print(v_name[0])
print("-----------------------------------")

v_job = jsonpath.jsonpath(v_jsonData,"job")
print(v_job[0])
print("-----------------------------------")

v_updatedAt = jsonpath.jsonpath(v_jsonData,"updatedAt")
print(v_updatedAt[0])


assert status_code == 200
assert v_input_name == v_name[0]
assert v_input_job == v_job[0]
assert v_updatedAt[0] is not None

