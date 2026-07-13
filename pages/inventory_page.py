from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    # Locators
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    # Methods
    def add_backpack(self):
        self.click(*self.BACKPACK)

    def add_bike_light(self):
        self.click(*self.BIKE_LIGHT)

    def open_cart(self):
        self.click(*self.CART_ICON)

    def get_cart_count(self):
        return self.find(*self.CART_BADGE).text