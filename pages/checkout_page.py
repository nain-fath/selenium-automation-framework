from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # Customer Information
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    # Buttons
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")

    # Success Message
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def enter_first_name(self, first_name):
        self.enter_text(*self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(*self.LAST_NAME, last_name)

    def enter_postal_code(self, postal_code):
        self.enter_text(*self.POSTAL_CODE, postal_code)

    def click_continue(self):
        self.click(*self.CONTINUE)

    def click_finish(self):
        self.click(*self.FINISH)

    def get_success_message(self):
        return self.find(*self.COMPLETE_HEADER).text