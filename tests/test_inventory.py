from utilities.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_product_to_cart(driver):

    config = ConfigReader.get_config()
    driver.get(config["base_url"])

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login(
    config["username"],
    config["password"]
)

    inventory.add_backpack()

    assert inventory.get_cart_count() == "1"