import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

desired_cap={
    "deviceName": "NLMR1T0129",
    "platformName": "Android",
    "app": "C:\\Users\\indrasen\\Documents\\Udemy\\Android_Demo_App.apk",
    "appPackage":"com.code2lead.kwad",
    "appActivity":"com.code2lead.kwad.MainActivity",
    "platformVersion":"9.0"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

ele1 = driver.find_element_by_id("com.code2lead.kwad:id/EnterValue")
ele2 = driver.find_element_by_id("com.code2lead.kwad:id/Login")

driver.scroll(ele2,ele1)
time.sleep(3)

actions = TouchAction(driver)
ele3 = driver.find_element_by_id("com.code2lead.kwad:id/LongClick")
#actions.tap(x=60,y=947).perform()
actions.tap(ele3)