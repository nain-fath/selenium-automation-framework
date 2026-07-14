from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID,"user-name")
    PASSWORD = (By.ID,"password")
    LOGIN = (By.ID,"login-button")

    def login(self, username, password):

        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN)