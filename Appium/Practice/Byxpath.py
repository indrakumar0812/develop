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
driver.find_element_by_xpath("//android.widget.Button[@content-desc='Btn1']").click()
time.sleep(2)
#driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.EditText").send_keys("codetolearn")
driver.find_element_by_xpath("//android.widget.EditText[@text='Enter some Value']").send_keys("codetolearn")