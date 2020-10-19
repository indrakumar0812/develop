import requests
from Udemy.utilities.config import ReadConfig


url = "https://api.github.com/user/repos"
url2 = "https://api.github.com/user"
config = ReadConfig()
usr = config.getUsername()
pwd =config.getPassword()

se = requests.session()
se.auth = auth=(usr,pwd)

se_resp = se.get(url)
se_resp1 = se.get(url2)
print(se_resp.status_code)
print(se_resp1.status_code)