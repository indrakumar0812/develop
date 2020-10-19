from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    #driver.find_element_by_id("country")
    #find_element_by_link_text("India")
    #driver.find_element_by_xpath("//div[contains(@class,'checkbox-primary')]")
    #driver.find_element_by_css_selector("input[type='submit']")
    #driver.find_element_by_css_selector(driver.find_element_by_css_selector("div[class*='alert-succes']"))

    country = (By.ID, "country")
    countryname = (By.LINK_TEXT,"India")
    checkbox = (By.XPATH, "//div[contains(@class,'checkbox-primary')]")
    purchase = (By.CSS_SELECTOR, "input[type='submit']")
    success = (By.CSS_SELECTOR,"div[class*='alert-succes']")

    def confirmPage(self):
        return self.driver.find_element(*ConfirmPage.country)
    def countryName(self):
        return self.driver.find_element(*ConfirmPage.countryname)
    def checkBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)
    def purchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase)
    def successMsg(self):
        return self.driver.find_element(*ConfirmPage.success)