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

ele = driver.find_element_by_id("com.code2lead.kwad:id/EnterValue")
print("Text of the button is:",ele.text)
print("Content description is:",ele.get_attribute("content-desc"))
ele.click()
time.sleep(3)
ele_text = driver.find_element_by_xpath("//android.widget.EditText[@text='Enter some Value']")
ele_text.send_keys("hello")
time.sleep(2)
ele_text.clear()