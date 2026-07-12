from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        self.find(by, value).click()

    def enter_text(self, by, value, text):
        element = self.find(by, value)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title