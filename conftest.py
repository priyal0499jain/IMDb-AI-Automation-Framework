import os
from datetime import datetime
import pytest
from utilities.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def driver():

    driver = DriverFactory.get_driver()

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshots/{item.name}_{timestamp}.png"

            driver.save_screenshot(filename)

            print(f"\nScreenshot saved: {filename}")