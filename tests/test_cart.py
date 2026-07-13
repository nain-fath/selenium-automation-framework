from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utilities.config_reader import ConfigReader


def test_remove_product_from_cart(driver):

    config = ConfigReader.get_config()
    driver.get(config["base_url"])

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.login(
    config["username"],
    config["password"]
)

    inventory.add_backpack()

    inventory.open_cart()

    assert cart.get_product_name() == "Sauce Labs Backpack"

    cart.remove_backpack()

    cart.continue_shopping()