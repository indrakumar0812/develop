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

driver.find_element_by_id("com.code2lead.kwad:id/TabView").click()

deviceSize = driver.get_window_size()
print(deviceSize)
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

####Right to Left#####
Startx = screenWidth*8/9 #...8 denotes 80% of the screen...#
Endx = screenWidth/9
Starty = screenHeight/2 #...Half the height of the Y axis which is constant...#
Endy = screenHeight/2 #...Half the height of the Y axis which is constant...#

####Left to Right ####
Startx2 = screenWidth/9
Endx2 = screenWidth*8/9
Starty2 = screenHeight/2
Endy2 = screenHeight/2

time.sleep(2)

actions = TouchAction(driver)
actions.long_press(None,Startx,Starty).move_to(None,Endx,Endy).release().perform()
time.sleep(2)
actions.long_press(None,Startx2,Starty2).move_to(None,Endx2,Endy2).release().perform()