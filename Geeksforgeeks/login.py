from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#ele = driver.find_element_by_id("//select[@id='dropdown-class-example']")
ele = driver.find_element_by_xpath("//button[text()='Home']")
ele.screenshot("drop.png")
ele.click()

#list1=driver.find_elements_by_xpath("//select[@id='dropdown-class-example']/option")

#print(list1)