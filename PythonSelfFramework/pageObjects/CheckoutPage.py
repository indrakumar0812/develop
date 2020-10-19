from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cartTitle = (By.CSS_SELECTOR, ".card-title a")
    #productName = (By.XPATH, "div/h4/a")
    cartButton = (By.CSS_SELECTOR, ".card-footer button")
    checkoutButton = (By.CSS_SELECTOR,"a[class*= 'btn-primary']")
    productTitle = (By.XPATH, "//h4[@class='media-heading']/a")
    checkoutSuccess = (By.XPATH, "//button[@class='btn btn-success']")

    def getCartTitles(self):
        return self.driver.find_elements(*CheckOutPage.cartTitle)

    #def getproductName(self):
       # return self.driver.find_element(*CheckOutPage.productName)

    def getcartButton(self):
        return self.driver.find_elements(*CheckOutPage.cartButton)

    def getcheckoutButton(self):
        return self.driver.find_element(*CheckOutPage.checkoutButton)

    def getproductTitle(self):
        return self.driver.find_element(*CheckOutPage.productTitle)

    def getcheckoutSuccess(self):
        self.driver.find_element(*CheckOutPage.checkoutSuccess).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
