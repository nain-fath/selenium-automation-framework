from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utilities.config_reader import ConfigReader
from utilities.logger import Logger


def test_add_product_to_cart(driver):

    # Read configuration
    config = ConfigReader.get_config()

    # Create logger
    logger = Logger.get_logger()

    # Open Website
    logger.info("Opening SauceDemo website")
    driver.get(config["base_url"])

    # Create Page Objects
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    # Login
    logger.info("Logging into the application")
    login.login(
        config["username"],
        config["password"]
    )

    # Add Product
    logger.info("Adding Backpack to cart")
    inventory.add_backpack()

    # Verify Cart Count
    logger.info("Verifying cart count")
    assert inventory.get_cart_count() == "1"

    logger.info("Inventory test completed successfully")