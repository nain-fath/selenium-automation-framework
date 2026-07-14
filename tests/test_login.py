from pages.login_page import LoginPage
from utilities.config import BASE_URL, USERNAME, PASSWORD

def test_valid_login(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    assert "inventory" in driver.current_url