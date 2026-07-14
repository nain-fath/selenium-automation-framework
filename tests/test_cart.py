from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utilities.config_reader import ConfigReader
from utilities.logger import Logger


def test_remove_product_from_cart(driver):

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
    cart = CartPage(driver)

    # Login
    logger.info("Logging into the application")
    login.login(
        config["username"],
        config["password"]
    )

    # Add Product
    logger.info("Adding Backpack to cart")
    inventory.add_backpack()

    # Open Cart
    logger.info("Opening cart")
    inventory.open_cart()

    # Verify Product
    logger.info("Verifying product in cart")
    assert cart.get_product_name() == "Sauce Labs Backpack"

    # Remove Product
    logger.info("Removing Backpack from cart")
    cart.remove_backpack()
    print("Current URL:", driver.current_url)
    print("Page Title:", driver.title)

    # Continue Shopping
    logger.info("Continuing shopping")
    cart.continue_shopping()

    logger.info("Cart test completed successfully")