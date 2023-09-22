from feactures.pageobjects.BasePage import BasePage


class LoginCredentialsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)

    def clickLoginHome(self):
        self.click("login_link_home_ID")

    def setLogin(self, login):
        self.type("login_XPATH", login)

    def setPassword(self, password):
        self.type("password_login_XPATH", password)

    def clickBtnEnter(self):
        self.click("enter_XPATH")

    def getValueUserLogged(self):
        return self.value("system_login_logged_ID")


