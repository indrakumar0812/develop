from selenium import webdriver
import requests


driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.google.com/")

links = driver.find_elements_by_tag_name("a")
print(len(links))
images = driver.find_elements_by_tag_name("img")
print(len(images))
links.extend(images)
size = len(links)
print("all links size is", size)
activeLinks =[]

for link in links:
    if link.get_attribute("href") != None:
        activeLinks.append(link)
print("no of active links is",len(activeLinks))

iterObj = iter(activeLinks)
for i in range(len(activeLinks)):
    url = next(iterObj).get_attribute("href")
    r = requests.head(url)

    if r.status_code == 404:
        print("broken link is:",url)

driver.close()




