import time

import pytest

from pageObjects.customersPage import Customers
from utilities.customLogger import LogGen
from utilities import ExcelUtils
from utilities.ExcelUtils import HomePageData

class Test_002_Customers():

    logs = LogGen.getLogger()

    def test_addCustomer(self,setup,getData):

        self.logs.info("---------Starting Test_002__Customers--------")
        self.logs.info("---------Entering User details--------")

        self.driver=setup
        self.cust = Customers(self.driver)

        self.logs.info("---------Clicking the Customers option--------")
        self.cust.clickCustomersmenu()
        time.sleep(2)
        self.cust.clickCustomersubmenu()
        self.cust.addCustomer()
        self.logs.info("---------Creating a new user--------")

        self.cust.getEmail(getData["email"])
        self.cust.getPassword(getData["pwd"])
        self.cust.getFirstName(getData["fname"])
        self.cust.getLastName(getData["lname"])

        #self.cust.getGender(getData["gender"])
        self.cust.getGender()
        self.cust.clickCalendar()
        time.sleep(4)
        current_year = self.cust.getCurrentYear()
        try:
            self.cust.getBirthdate(getData["year"],getData["month"],getData["day"],current_year)
        except Exception as ValueError:
            self.logs.warning("--------Exception has occured--------")
        time.sleep(3)
        self.cust.getCompanyname(getData["cname"])
        self.cust.selTaxExempt(getData["tax"])
        self.driver.implicitly_wait(4)
        self.cust.getNewsLetter()
        self.cust.getNewsLetterChoice(getData["newsletter"])
        self.cust.getCustomerRoles()
        self.driver.implicitly_wait(4)
        self.cust.getCustomerRolesOption(getData["custroles"])
        self.cust.getVendorDetails(getData["vendor"])
        self.cust.getActivestatus(getData["active"])
        self.cust.getAdminComments(getData["admcomment"])
        self.cust.createCustomer()
        self.logs.info("---------New Customer Created--------")


    @pytest.fixture(params=HomePageData.getTestData('customerDetails'))
    #@pytest.fixture(params=HomePageData.test_data)
    def getData(self,request):
        return request.param
