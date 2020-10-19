import time
import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        logs = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        #checkOutPage = CheckOutPage(self.driver)
        logs.info("getting cart titles")
        products = checkoutpage.getCartTitles()
        logs.info(products)
        #self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        i = -1
        for cards in products:
            i = i+1
            productname = cards.text
            #i.find_element_by_xpath("div/h4/a").text
            logs.info(productname)
            if productname == "Blackberry":
                checkoutpage.getcartButton()[i].click()
                #i.find_element_by_xpath("div[2]/button").click()
        checkoutpage.getcheckoutButton().click()
        #self.driver.find_element_by_css_selector("a[class*= 'btn-primary']").click()
        final = checkoutpage.getproductTitle().text

        assert productname == final

        confirmpage = checkoutpage.getcheckoutSuccess()
        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        #self.driver.find_element_by_id("country").send_keys("ind")
        logs.info("entering country name")
        #confirmpage = ConfirmPage(self.driver)
        confirmpage.confirmPage().send_keys("ind")
        self.LinkPresence("India")
        #wait = WebDriverWait(self.driver, 6)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        confirmpage.countryName().click()
        confirmpage.checkBox().click()
        confirmpage.purchaseButton().click()
        successText = confirmpage.successMsg().text
        logs.info("text match is:" +successText)
        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")

