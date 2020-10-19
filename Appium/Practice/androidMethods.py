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

print("app package:",driver.current_package)
print("app activity:",driver.current_activity)
print("device locked:",driver.is_locked())
print("current context:",driver.current_context)
print("current orientation:",driver.orientation)