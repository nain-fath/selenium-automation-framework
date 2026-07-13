from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, by, value):
        return self.wait.until(
            EC.visibility_of_element_located((by, value))
        )

    def click(self, by, value):
        self.wait.until(
            EC.element_to_be_clickable((by, value))
        ).click()

    def enter_text(self, by, value, text):
        element = self.find(by, value)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title