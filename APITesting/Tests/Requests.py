import requests

test_url = "https://reqres.in/"

v_data = requests.get(test_url)

print(v_data)
print("-------------------------------------")
print(v_data.status_code)
print("-------------------------------------")
print(v_data.text)
print("-------------------------------------")
print(v_data.headers)

