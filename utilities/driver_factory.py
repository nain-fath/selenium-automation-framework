import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver(browser="chrome"):

    browser = browser.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()

        # Local browser settings
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")

        # GitHub Actions settings
        if os.getenv("GITHUB_ACTIONS") == "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        }

        options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options,
        )

    elif browser == "edge":
        options = webdriver.EdgeOptions()

        options.add_argument("--start-maximized")

        if os.getenv("GITHUB_ACTIONS") == "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options,
        )

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(5)

    return driver