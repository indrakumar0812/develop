import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import select, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Customers:

    def __init__(self,driver):
        self.driver=driver

    menuoptions_customers_xpath = (By.XPATH,'//ul[@class="sidebar-menu tree"]/li[4]')
    menuSuboptions_customers_xpath = (By.XPATH,'//a[@href="/Admin/Customer/List"]/span')
    button_addcustomer_xpath = (By.XPATH,'//a[@href="/Admin/Customer/Create"]')
    textbox_email_id=(By.ID,'Email')
    textbox_password_id = (By.ID,'Password')
    textbox_firstName_id =(By.ID,'FirstName')
    textbox_lastName_id = (By.ID,'LastName')
    #radiobutton_gender_css = (By.CSS_SELECTOR,'input[name="Gender"]')#list
    radiobutton_gender_css = (By.CSS_SELECTOR,'input[id = "Gender_Male"]')

    button_calendar_css = (By.CSS_SELECTOR,'span[aria-controls="DateOfBirth_dateview"]')
    button_year_css = (By.CSS_SELECTOR,'a[class*="k-nav-fast"]')
    button_previous_css =(By.CSS_SELECTOR,'a[class*="k-nav-prev"]')
    button_months_css = (By.CSS_SELECTOR,'a[class="k-link"]') #list
    button_date_xpath = (By.XPATH,'//div[@class="k-calendar-view"]/table/tbody/tr/td') #list
    textbox_companyName_id = (By.ID,'Company')
    checkbox_taxExempt_id =(By.ID,'IsTaxExempt')
    listbox_newsletter_xpath = (By.XPATH,'//div[@class="panel-body"]/div[9]/div[2]/div[1]/div[1]')
    listboxOptions_newsletter_xpath = (By.XPATH,'//div[contains(@id,"StoreIds-list")]/div[2]/ul/li') #list
    listbox_customerRoles_xpath = (By.XPATH,'//div[@class="panel-body"]/div[9]/div[2]/div[1]/div[1]')
    listboxOptions_customerRoles_xpath = (By.XPATH,'//div[contains(@id,"RoleIds-list")]/div[2]/ul/li')
    dropdownbox_vendor_id = (By.ID,'VendorId')
    checkbox_active_id = (By.ID,'Active')
    textbox_admincomment_id = (By.ID,'AdminComment')
    button_save_css = (By.CSS_SELECTOR,'button[name="save"]')

    def clickCustomersmenu(self):
        self.driver.find_element(*Customers.menuoptions_customers_xpath).click()

    def clickCustomersubmenu(self):
        self.driver.find_element(*Customers.menuSuboptions_customers_xpath).click()

    def addCustomer(self):
        self.driver.find_element(*Customers.button_addcustomer_xpath).click()

    def getEmail(self,email):
        self.driver.find_element(*Customers.textbox_email_id).send_keys(email)

    def getPassword(self,password):
        self.driver.find_element(*Customers.textbox_password_id).send_keys(password)

    def getFirstName(self,fname):
        self.driver.find_element(*Customers.textbox_firstName_id).send_keys(fname)

    def getLastName(self,lname):
        self.driver.find_element(*Customers.textbox_lastName_id).send_keys(lname)

    def getGender(self):
        #c_gender = self.driver.find_elements(*Customers.radiobutton_gender_css)
        self.driver.find_element(*Customers.radiobutton_gender_css).click()

        #for i in c_gender:
        #    if i.getAttribute("value") == data:
         #      i.click()

    def clickCalendar(self):
        self.driver.find_element(*Customers.button_calendar_css).click()

    def getCurrentYear(self):
        self.driver.find_element(*Customers.button_year_css).click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.presence_of_element_located(Customers.button_year_css))
        ele = self.driver.find_element(*Customers.button_year_css)
        current_year = int(ele.text)
        return current_year

    #def getPreviousYear(self,year,month,day):

    def getBirthdate(self,year,month,value,current_year):

        n = current_year-year

        i =0
        while(i<n):
            self.driver.find_element(*Customers.button_previous_css).click()
            i+=1

    #def getMonth(self,month):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located(Customers.button_months_css))
        birth_month = self.driver.find_elements(*Customers.button_months_css)

        for i in birth_month:
            if i.text == month:
                i.click()

    #def getDate(self,value):

        days = self.driver.find_elements(*Customers.button_date_xpath)

        for i in days:
            if int(i.text) == value:
                i.click()

    def getCompanyname(self,cmpname):

        self.driver.find_element(*Customers.textbox_companyName_id).send_keys(cmpname)

    def selTaxExempt(self,tax_eligibility):

        if tax_eligibility == "Yes":
            self.driver.find_element(*Customers.checkbox_taxExempt_id).click()

        if tax_eligibility == "No" or " ":
            print("customer is not eligibile for tax")

    def getNewsLetter(self):

        a = self.driver.find_element(*Customers.listbox_newsletter_xpath)
        a.click()

    def getNewsLetterChoice(self,choice):

        choices = self.driver.find_elements(*Customers.listboxOptions_newsletter_xpath)

        for i in choices:
            if i.text==choice:
                i.click()

    def getCustomerRoles(self):

        a = self.driver.find_element(*Customers.listbox_customerRoles_xpath)
        a.click()

    def getCustomerRolesOption(self,role):

        roles = self.driver.find_elements(*Customers.listboxOptions_customerRoles_xpath)

        for i in roles:
            if i.text == role:
                i.click()

    def getVendorDetails(self,value):

        vendor = self.driver.find_element(*Customers.dropdownbox_vendor_id)

        sel = Select(vendor)
        sel.select_by_index(value)


    def getActivestatus(self,status):

        if status == "No":

            self.driver.find_element(*Customers.checkbox_active_id).click()
        elif status == "Yes":
            print("Customer status is active")

    def getAdminComments(self,texts):

        self.driver.find_element(*Customers.textbox_admincomment_id).send_keys(texts)

    def createCustomer(self):

        self.driver.find_element(*Customers.button_save_css).click()



