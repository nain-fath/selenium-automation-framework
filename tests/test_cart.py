from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_remove_product_from_cart(driver):

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.login("standard_user", "secret_sauce")

    inventory.add_backpack()

    inventory.open_cart()

    assert cart.get_product_name() == "Sauce Labs Backpack"

    cart.remove_backpack()

    cart.continue_shopping()