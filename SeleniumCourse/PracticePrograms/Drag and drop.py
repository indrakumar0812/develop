import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
time.sleep(6)
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[class='demo-frame']"))
source = driver.find_element_by_id("draggable")
destination = driver.find_element_by_id("droppable")
act = ActionChains(driver)
act.drag_and_drop(source,destination).perform()