from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        # Scroll element into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        # Normal click
        try:
            element.click()
        except Exception:
            # Fallback JavaScript click
            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    def enter_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title