import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        logs = self.getLogger()
        homePage = HomePage(self.driver)
        #homePage.getName().send_keys(getData[0])
        logs.info("name is:" +getData["name"])
        homePage.getName().send_keys(getData["name"])
        #homePage.getEmail().send_keys(getData[1])
        homePage.getEmail().send_keys(getData["email"])
        homePage.clickCheckBox().click()
        #self.selectOptionByText(homePage.selDropBox(),getData[2])
        self.selectOptionByText(homePage.selDropBox(),getData["gender"])
        #sel = Select(homePage.selDropBox())
        #sel.select_by_visible_text("Male")
        homePage.clickSubmit().click()
        alertText = homePage.alertMsg().text

        assert ("Success!" in alertText)
        self.driver.refresh()

    #@pytest.fixture(params=[("Ram","abc@gmail.com","Male"),("Simran","xyz@gmail.com","Female")])
    #@pytest.fixture(params=HomePageData.test_HomePage_data)
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self,request):
        print(request.param)
        return request.param
