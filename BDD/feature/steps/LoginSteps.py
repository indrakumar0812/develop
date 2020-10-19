from behave import *
from selenium import webdriver

@given('I launch the chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when('I open the HRM home page')
def HomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{usr}" and password "{pwd}"')
def enterCredentials(context,usr,pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(usr)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when('click on the login button')
def clickLoginButton(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('User must successfully login to the dashboard')
def dashboardDisplay(context):
    try:
        text1=context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except Exception as e:
        context.driver.close()
        assert False

    if text1 == "Dashboard":
        assert True
        context.driver.close()


