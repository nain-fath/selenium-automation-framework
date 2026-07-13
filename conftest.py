import os
from datetime import datetime

import pytest
from utilities.driver_factory import get_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome, edge, firefox"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    driver = get_driver(browser)

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