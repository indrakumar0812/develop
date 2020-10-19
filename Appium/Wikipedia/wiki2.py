import time

from selenium import webdriver
from appium import webdriver


desired_cap= {
        "deviceName": "NLMR1T0129",
        "platformName": "Android",
        "appPackage": "org.wikipedia",
        "appActivity": "org.wikipedia.main.MainActivity",
        "platformVersion": "9.0"
    }

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.press_keycode(4)
driver.find_element_by_id("org.wikipedia:id/search_container").click()
driver.find_element_by_id("org.wikipedia:id/search_src_text").send_keys("official language of India")
driver.hide_keyboard()
time.sleep(2)
driver.swipe(232,1292,232,505)
search_list = driver.find_elements_by_id("org.wikipedia:id/page_list_item_title")
time.sleep(2)

for i in search_list:
    if i.text == "Hindi":
        i.click()
        break

time.sleep(2)
driver.find_element_by_id("org.wikipedia:id/article_menu_bookmark").click()

for i in range (3):
    driver.press_keycode(4)
    time.sleep(1)

#app_view = driver.contexts
#for i in app_view:
#    print(i)

driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='My lists']").click()
driver.find_element_by_id("org.wikipedia:id/negativeButton").click()
driver.find_element_by_id("org.wikipedia:id/item_title").click()


list = driver.find_elements_by_id("org.wikipedia:id/page_list_item_title")
time.sleep(2)

for i in list:
    if i.text == "Hindi":
        print("Test case has passed")
        break