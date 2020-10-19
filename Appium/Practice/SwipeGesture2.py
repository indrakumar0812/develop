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

driver.find_element_by_id("com.code2lead.kwad:id/ScrollView").click()

deviceSize = driver.get_window_size()
print(deviceSize)
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

####t bottom to top #####
Startx = screenWidth/2 #...Half of the x axis which is constant...#
Endx = screenWidth/2
Starty = screenHeight*8/9 #..Swiping up across the Y axis from the 80% of the screen..#
Endy = screenHeight*2/9

#### top to bottom ####
Startx2 = screenWidth/2
Endx2 = screenWidth/2
Starty2 = screenHeight*2/9 #..using 20% to avoid the swiping from the notification curtains...#
Endy2 = screenHeight*8/9

time.sleep(2)

actions = TouchAction(driver)
actions.long_press(None,Startx,Starty).move_to(None,Endx,Endy).release().perform()
time.sleep(2)
actions.long_press(None,Startx2,Starty2).move_to(None,Endx2,Endy2).release().perform()