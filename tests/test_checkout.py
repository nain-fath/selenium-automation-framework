from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utilities.config_reader import ConfigReader


def test_complete_checkout(driver):

    config = ConfigReader.get_config()
    driver.get(config["base_url"])

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Login
    login.login(
    config["username"],
    config["password"]
)
    print("After Login:", driver.current_url)

    # Add product
    inventory.add_backpack()
    print("Cart Count:", inventory.get_cart_count())

    # Open cart
    inventory.open_cart()
    print("After Open Cart:", driver.current_url)

    # Verify product
    print("Product:", cart.get_product_name())

    # Check if checkout button exists
    from selenium.webdriver.common.by import By

    checkout_buttons = driver.find_elements(By.ID, "checkout")
    print("Checkout buttons found:", len(checkout_buttons))

    if checkout_buttons:
        print("Checkout button displayed:", checkout_buttons[0].is_displayed())
        print("Checkout button enabled:", checkout_buttons[0].is_enabled())

    # Click checkout
    cart.click_checkout()

    print("After Checkout Click:", driver.current_url)

    # Fill details
    checkout.enter_first_name("Kaunain")
    checkout.enter_last_name("Fathima")
    checkout.enter_postal_code("560001")

    checkout.click_continue()
    checkout.click_finish()

    assert checkout.get_success_message() == "Thank you for your order!"