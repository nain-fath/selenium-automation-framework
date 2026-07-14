from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utilities.config_reader import ConfigReader
from utilities.logger import Logger


def test_complete_checkout(driver):

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
    checkout = CheckoutPage(driver)

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

    # Checkout
    logger.info("Proceeding to checkout")
    cart.click_checkout()

    assert "checkout-step-one" in driver.current_url
    print("Current URL:", driver.current_url)
    print("Page Title:", driver.title)

    # Customer Information
    logger.info("Entering customer information")
    checkout.enter_first_name("Kaunain")
    checkout.enter_last_name("Fathima")
    checkout.enter_postal_code("560001")

    # Continue
    logger.info("Continuing checkout")
    checkout.click_continue()

    # Finish
    logger.info("Finishing order")
    checkout.click_finish()

    # Verify Success
    logger.info("Verifying success message")
    assert checkout.get_success_message() == "Thank you for your order!"

    logger.info("Checkout test completed successfully")