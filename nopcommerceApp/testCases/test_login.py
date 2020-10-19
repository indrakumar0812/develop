import time

import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils

class Test_001_Login():

    #baseurl="https://admin-demo.nopcommerce.com/"
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logs = LogGen.getLogger()

    def test_HomePageTitle(self,setup):

        self.logs.info("------------Test_001_Login-----------")
        self.logs.info("------------Verifying Home Page Title------------")

        self.driver = setup
        #self.driver.get(self.baseurl)
        acct_title= self.driver.title

        if acct_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logs.info("------------Home Page Title verification Successful--------------")

        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\"+"test_HomePageTitle.png")
            self.driver.close()
            self.logs.error("------------Home Page Title Verification Failed--------------")
            assert False


    def test_login(self,setup):

        self.logs.info("--------------Verifying Login Test--------------")
        self.driver = setup
        #self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        acct_title = self.driver.title

        if acct_title == "Dashboard / nopCommerce administration":
            assert True
            self.lp.clickLogout()
            self.driver.close()
            self.logs.info("---------------Login Successful--------------")
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logs.error("---------------Login Failed--------------")
            assert False


    def test_login_dd(self,setup,getData):

        list =[]

        self.logs.info("-------------Login Data validation Test start-----------")
        self.logs.info("--------------Verifying Login DD Test--------------")
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.setUserName(getData["username"])
        self.lp.setPassword(getData["password"])
        self.lp.clickLogin()
        time.sleep(5)
        acct_title = self.driver.title

        if acct_title == "Dashboard / nopCommerce administration":
            if getData["exp"]== "Pass":
                assert True
                self.lp.clickLogout()
                list.append("Pass")
                self.logs.info("---------------Passed--------------")
            elif getData["exp"] == "Fail":
                list.append("Fail")
                self.lp.clickLogout()
                self.logs.error("---------------Failed--------------")
                assert False
        elif acct_title != "Dashboard / nopCommerce administration":
                if getData["exp"]=="Fail":
                    list.append("Pass")
                    self.logs.info("---------Passed----------")
                elif getData["exp"]=="Pass":
                    list.append("Fail")
                    self.logs.info("---------Failed----------")


        if "Fail" not in list:
            self.logs.info("-------------Data Validation Test Passed------------")
            self.driver.close()
            assert True
        else:
            self.logs.error("------------Data Validation test failed------------")
            self.driver.close()
            assert False

        self.logs.info("----------End of Login DDT Test----------")
        self.logs.info("----------test_login_dd completed----------")


    @pytest.fixture(params=ExcelUtils.getTestData("loginDD"))
    def getData(self,request):
        return request.param
