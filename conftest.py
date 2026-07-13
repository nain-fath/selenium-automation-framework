import os
from datetime import datetime

import pytest
from utilities.driver_factory import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            screenshot_dir = "screenshots"

            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            file_name = f"{item.name}_{timestamp}.png"

            driver.save_screenshot(
                os.path.join(screenshot_dir, file_name)
            )