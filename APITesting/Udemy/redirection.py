import requests


url="http://rahulshettyacademy.com"

resp = requests.get(url)

print(resp.history) ##gives the redirection codes to which the target URL is redirected to. Status code of 300 mean
                    ### redirection
print(resp.status_code)

print("---------------------------------------")

#allow_redirects=False argument tells whether a URL is redirected or not by giving the 300 status code, normally if the endoint
#is being hit directly then it should return 200 status code. In this case it returns 301 coz the url is being re-directed
#so it returns the status code 301 and stops it.
resp1 = requests.get(url,allow_redirects=False)
print(resp1.status_code)

print("---------------------------------------")

#timeout=1 arguments means that it will wait for 1s before hitting the url
resp2 = requests.get(url,allow_redirects=False,timeout=1)
print(resp2.status_code)