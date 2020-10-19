import inspect
import logging

class LogGen:

    @staticmethod
    def getLogger():

        loggerName = inspect.stack()[1][3]  # will give the name of the method from where getLogger is called
        logger = logging.getLogger(loggerName)  # to retrive the test file name

        fileHandler = logging.FileHandler(".\\Logs\\automation.log")  # where the logs are stored

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object(file location)

        logger.setLevel(logging.DEBUG)  # set the debug level to info and only the error after
        # the info will be displayed and not debug levels
        return logger

