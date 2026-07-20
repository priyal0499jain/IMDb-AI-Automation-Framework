from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def press_enter(self, locator):
        self.find_element(locator).send_keys(Keys.ENTER)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, text):
        self.wait.until(
            EC.url_contains(text)
        )

    def wait_for_title_contains(self, text):
        self.wait.until(
            EC.title_contains(text)
        )

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

    def take_screenshot(self, file_name):
        self.driver.save_screenshot(
            f"screenshots/{file_name}.png"
        )