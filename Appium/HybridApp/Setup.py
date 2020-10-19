import time

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

desired_cap={
    "deviceName": "NLMR1T0129",
    "platformName": "Android",
    "appPackage":"com.android.chrome",
    "appActivity":"com.google.android.apps.chrome.Main",
    "platformVersion":"9.0"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

wait = WebDriverWait(driver,20,poll_frequency=2)

wait.until(lambda x:x.find_element_by_id("com.android.chrome:id/terms_accept")).click()
wait.until(lambda x:x.find_element_by_id("com.android.chrome:id/next_button")).click()
wait.until(lambda x:x.find_element_by_id("com.android.chrome:id/negative_button")).click()
wait.until(lambda x:x.find_element_by_id("com.android.chrome:id/search_box_text")).click()
url = wait.until(lambda x:x.find_element_by_id("com.android.chrome:id/url_bar"))
url.click()
url.send_keys("http://dummypoint.com/seleniumtemplate.html")
driver.press_keycode(66)

time.sleep(5)

appcontexts = driver.contexts
print(appcontexts)

for appType in appcontexts:
    if appType == "WEBVIEW_chrome":
        driver.switch_to.context(appType)
        print("In Webview")
        

eleTextBox = wait.until(lambda x:x.find_element_by_id("user_input"))
eleTextBox.click()
eleTextBox.send_keys("Codetolearn")

for appType in appcontexts:
    if appType == "NATIVE_APP":
        driver.switch_to.context(appType)
        print("In Native app")

url.click()
url.send_keys("http://www.kennisworld.com/")
driver.press_keycode(66)