import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
HomeProductsName=[]
for button in buttons:
    homePageProducts = button.find_element_by_xpath("parent::div/parent::div/h4")

    HomeProductsName.append(homePageProducts.text)
    button.click()

print(HomeProductsName)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,6)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoCode")))
productamt = driver.find_elements_by_xpath("//tr/td[5]/p")

tolsum=0
for amt in productamt:
   tolsum = tolsum+int(amt.text)

FinalProductsName =[]
CheckOutProducts = driver.find_elements_by_css_selector("p.product-name")

for finalproducts in CheckOutProducts:
    FinalProductsName.append(finalproducts.text)
print(FinalProductsName)
totalAmnt= driver.find_element_by_css_selector("span.totAmt").text
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
discountAmnt= driver.find_element_by_css_selector("span.discountAmt").text
print(driver.find_element_by_class_name("promoInfo").text)
assert tolsum == int(totalAmnt)
assert float(discountAmnt) < float(totalAmnt)
assert HomeProductsName == FinalProductsName