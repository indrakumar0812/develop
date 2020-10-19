import pytest
from selenium import webdriver

#passing the command line arguments
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name") #to get the browser name during runtime
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")

    elif browser_name == "firefox": #firefox gecko driver
        #driver = webdriver.Firefox(executable_path="C:\\Users\\indrasen\\Documents\\geckodriver-v0.26.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(executable_path="C:\\Users\\indrasen\\Downloads\\geckodriver-v0.26.0-win32\\geckodriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.close()