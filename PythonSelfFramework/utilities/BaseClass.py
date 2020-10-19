import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def LinkPresence(self, text):
        wait = WebDriverWait(self.driver, 6)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,element,text):
        sel = Select(element)
        sel.select_by_visible_text(text)
    

    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # will give the name of the method from where getLogger is called
        logger = logging.getLogger(loggerName)  # to retrive the test file name

        fileHandler = logging.FileHandler('logfile.log')  # where the logs are stored

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object(file location)

        logger.setLevel(logging.DEBUG)  # set the debug level to info and only the error after
        # the info will be displayed and not debug levels
        return logger