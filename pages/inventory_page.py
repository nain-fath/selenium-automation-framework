from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")

    def add_backpack(self):
        self.click(*self.BACKPACK)

    def remove_backpack(self):
        self.click(*self.REMOVE_BACKPACK)

    def get_cart_count(self):
        return self.find(*self.CART_BADGE).text