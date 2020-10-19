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

wait = WebDriverWait(driver,20)
wait.until(lambda x:x.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))')).click()

ele_keyword = wait.until(lambda x:x.find_element_by_id("com.code2lead.kwad:id/ingvw"))
ele_layout = wait.until(lambda x:x.find_element_by_id("com.code2lead.kwad:id/layout2"))

actions = TouchAction(driver)
actions.long_press(ele_keyword).move_to(ele_layout).release().perform()
time.sleep(5)
driver.quit()


