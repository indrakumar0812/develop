from behave import *
from selenium import webdriver


@given('Launch the chrome browser')
def launchBrowser(context):
    #context.driver=webdriver.Chrome()
    context.driver=webdriver.Chrome()

@when('open HRM home page')
def openHomePage(context):
   context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('Verify that the logo is displayed')
def verifyLogo(context):
    status= context.driver.find_element_by_xpath("//div[@id='divLogo']/img").is_displayed()
    assert status == True


@then('close the browser')
def closeBrowser(context):
   context.driver.close()

