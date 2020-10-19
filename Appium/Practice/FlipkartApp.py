import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

desired_cap={
    "deviceName": "NLMR1T0129",
    "platformName": "Android",
    "app": "C:\\Users\\indrasen\\Documents\\flipkart\\Flipkart Online Shopping App_v6.3.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.implicitly_wait(3)

driver.find_element_by_id("com.flipkart.android:id/btn_skip").click()
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Open Drawer']").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='All Categories']").click()
driver.find_element_by_xpath("//android.widget.ImageView[@bounds='[480,184][720,440]']").click()
driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView[1]").click()
time.sleep(2)
action = TouchAction(driver)
action.press(x=353, y=1171).wait(500).move_to(x=353, y=429).release().perform()
#driver.swipe()
time.sleep(2)
action.tap(x=175,y=1258).perform()
not_now = driver.find_element_by_id("com.flipkart.android:id/not_now_button")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.ID,'com.flipkart.android:id/not_now_button')))
not_now.click()



