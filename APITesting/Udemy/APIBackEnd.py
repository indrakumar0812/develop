import requests
import json
import jsonpath

#response = requests.get("https://reqres.in/api/users?page=someid",params={'page':'2'},)

response = requests.get("http://216.10.245.166/Library/GetBook.php",params={'AuthorName':'john foe'})

#print(response.status_code)
#print(response.headers)

res_data=response.json()

print(res_data[0])


