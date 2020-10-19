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
buttons = driver.find_elements_by_class_name("android.widget.Button")
print(len(buttons))

for i in buttons:
    if i.text == "ScrollView":
        i.click()
        break