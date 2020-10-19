import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\indrasen\\PycharmProjects\\APITesting\\Udemy\\configurations.ini")
class ReadConfig:

    @staticmethod
    def getUrl():
        baseURL= config.get("API","url")
        return baseURL

    def getAuthUrl(self):
        authUrl= config.get("API","AuthUrl")
        return authUrl

    def getUsername(self):
        usrname= config.get("Authentication","username")
        return usrname

    def getPassword(self):
        pwd=config.get("Authentication","password")
        return pwd