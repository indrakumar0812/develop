import time

from appium import webdriver

desired_cap={
    "deviceName": "NLMR1T0129",
    "platformName": "Android",
    "app": "C:\\Users\\indrasen\\Documents\\Udemy\\Android_Demo_App.apk",
    "appPackage":"com.code2lead.kwad",
    "appActivity":"com.code2lead.kwad.MainActivity",
    "platformVersion":"9.0"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.find_element_by_id("com.code2lead.kwad:id/EnterValue").click()
time.sleep(3)
ele = driver.find_element_by_xpath("//android.widget.EditText[@text='Enter some Value']")
#ele = driver.find_element_by_android_uiautomator('new UiSelector().text("Enter some Value")')
ele.send_keys("hello")
ele.click()

for i in range (2):
    driver.press_keycode(67)
    time.sleep(1)

for i in range (2):
    driver.press_keycode(4)