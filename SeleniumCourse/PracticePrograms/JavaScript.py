import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_xpath("//form[contains(@class,'ng-pristine')]/div//input[@name='name']").send_keys("indrasen")
#time.sleep(2)
driver.find_element_by_name("name").send_keys("indrasen")
print(driver.find_element_by_name("name").get_attribute("value"))
driver.find_element_by_xpath("//input[@name='email']").send_keys("abc@gmail.com")
print(driver.find_element_by_xpath("//input[@name='email']").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("email")[0].value'))
#NameValue = driver.find_element_by_xpath("//form[contains(@class,'ng-pristine')]/div//input[@name='name']").get_attribute("value")
#print(NameValue)
#pwd = driver.find_element_by_id("exampleInputPassword1")
#driver.execute_script("arguments[0].send_keys("test");",pwd)-->wouldn't support
shopButton = driver.find_element_by_xpath("//a[contains(@href,'shop')]")
driver.execute_script("arguments[0].click();",shopButton)
driver.quit()
