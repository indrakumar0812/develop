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
print("Is displayed:",ele.is_displayed())
print("Is enabled:",ele.is_enabled())
print("Is selected:",ele.is_selected())
print("Size:",ele.size)
print("Location:",ele.location)