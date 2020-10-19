import requests

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"

files = {'file': open('C:\\Users\\indrasen\\Documents\\Pets.jpg', 'rb')}

r = requests.post(url,files=files)
print(r.status_code)
print(r.text)