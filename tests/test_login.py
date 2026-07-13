from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader
from utilities.logger import Logger


def test_valid_login(driver):

    # Read configuration
    config = ConfigReader.get_config()

    # Create logger
    logger = Logger.get_logger()

    # Open website
    logger.info("Opening SauceDemo website")
    driver.get(config["base_url"])

    # Create Login Page Object
    login = LoginPage(driver)

    # Login
    logger.info("Logging into the application")
    login.login(
        config["username"],
        config["password"]
    )

    # Verify Login
    logger.info("Verifying successful login")
    assert "inventory" in driver.current_url

    logger.info("Login test completed successfully")