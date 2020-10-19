import requests

cookie = {'visit-month':'February'}
url="http://rahulshettyacademy.com"

resp = requests.get(url,cookies=cookie)
print(resp.status_code)

print("-----------------------------------------------------------")
se = requests.session()
se.cookies.update(cookie)
url2= "https://httpbin.org/cookies"

### here the cookie={'visit-year':'2022'} will change but the cookie={'visit-month':'February'} is constant
### so we have added it in the session manager

resp1 = se.get(url2,cookies={'visit-year':'2022'})
print(resp1.text)