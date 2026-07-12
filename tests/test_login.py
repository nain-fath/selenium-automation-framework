from utilities.driver_factory import get_driver

def test_open_saucedemo():
    driver = get_driver()

    driver.get("https://www.saucedemo.com")

    assert "Swag Labs" in driver.title

    driver.quit()