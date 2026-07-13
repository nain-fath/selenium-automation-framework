from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_product_to_cart(driver):

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")

    inventory.add_backpack()

    assert inventory.get_cart_count() == "1"