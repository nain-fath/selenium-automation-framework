from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT = (By.ID, "checkout")

    def get_product_name(self):
        return self.find(self.CART_ITEM).text

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)

    def click_checkout(self):
        self.click(self.CHECKOUT)