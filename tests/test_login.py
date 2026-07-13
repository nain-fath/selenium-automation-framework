from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader


def test_valid_login(driver):

    config = ConfigReader.get_config()

    driver.get(config["base_url"])

    login = LoginPage(driver)

    login.login(
        config["username"],
        config["password"]
    )

    assert "inventory" in driver.current_url