import time

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

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
wait = WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
ele = wait.until(lambda x:x.find_element_by_android_uiautomator('UiSelector().text("ScrollView")'))
ele.click()
time.sleep(2)
driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))').click()
