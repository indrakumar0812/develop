from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.XPATH, "//form[contains(@class,'ng-untouched')]/div[1]/input")
    email = (By.NAME,"email")
    checkbox = (By.ID, "exampleCheck1")
    dropbox = (By.ID, "exampleFormControlSelect1")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    alert = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def shopItems(self):
       #return self.driver.find_element(*HomePage.shop) #* to de-serialize #driver.find_element_by_css_selector("a[href*='shop']")
       self.driver.find_element(*HomePage.shop).click()
       checkOutPage = CheckOutPage(self.driver)
       return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def clickCheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def selDropBox(self):
        return self.driver.find_element(*HomePage.dropbox)

    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def alertMsg(self):
        return self.driver.find_element(*HomePage.alert)