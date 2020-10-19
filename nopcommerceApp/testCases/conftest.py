import time

import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from pageObjects.loginPage import Login


baseurl=ReadConfig.getUrl()
username = ReadConfig.getUsername()
password = ReadConfig.getPassword()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
        print("Launching Chrome browser....")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\indrasen\\Downloads\\geckodriver-v0.27.0-win64\\geckodriver.exe")
        print("Launching firefox browser....")

    driver.get(baseurl)
    driver.maximize_window()
    lp = Login(driver)

    lp.setUserName(username)
    lp.setPassword(password)
    lp.clickLogin()
    time.sleep(2)

    return driver


############### Pytest HTML Report ################

#It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Indrasen'

#It is hook for delete/modify Environment info to Html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

################Login in the application#####################


