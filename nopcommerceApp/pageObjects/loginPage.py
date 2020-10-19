from selenium.webdriver.common.by import By

class Login:

    def __init__(self,driver):
        self.driver=driver

    textbox_email_id = (By.ID,"Email")
    textbox_password_id = (By.ID,"Password")
    button_login_css = (By.CSS_SELECTOR,"input[type='submit']")
    link_logout_linktext = (By.LINK_TEXT,"Logout")

    def setUserName(self,username):
        self.driver.find_element(*Login.textbox_email_id).clear()
        self.driver.find_element(*Login.textbox_email_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(*Login.textbox_password_id).clear()
        self.driver.find_element(*Login.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*Login.button_login_css).click()

    def clickLogout(self):
        self.driver.find_element(*Login.link_logout_linktext).click()