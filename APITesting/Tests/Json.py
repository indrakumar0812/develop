import jsonpath
import json

v_pointer = open("C:\\Users\\indrasen\\Downloads\\API\\sample_json.json",mode ='r')

data = v_pointer.read()

print(type(data))
print("--------------------------------------------------------------------")
json_data = json.loads(data)
print(type(json_data))
print("--------------------------------------------------------------------")
print(json_data)
d1 = jsonpath.jsonpath(json_data,"class")
d2 = jsonpath.jsonpath(json_data,"School")
d3 = jsonpath.jsonpath(json_data,"Students")
d4 = jsonpath.jsonpath(json_data,"Students[0]")
d5 = jsonpath.jsonpath(json_data,"Students[*].Name")
d6 = jsonpath.jsonpath(json_data,"Students[0,1].ID")
d7 = jsonpath.jsonpath(json_data,"Students[0:-1].Age")
print(d1)
print("--------------------------------------------------------------------")
print(d2)
print("--------------------------------------------------------------------")
print(d3)
print("--------------------------------------------------------------------")
print(d4)
print("--------------------------------------------------------------------")
print(d5)
print("--------------------------------------------------------------------")
print(d6)
print("--------------------------------------------------------------------")
print(d7)


assert  d5[1] == 'Abhay'