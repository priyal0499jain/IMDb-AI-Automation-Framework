from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from config.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def get_driver():

        browser = ConfigReader.get_browser()

        options = Options()

        if ConfigReader.is_headless():
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")

        if browser.lower() == "chrome":

            driver = webdriver.Chrome(
                service=Service(
                    ChromeDriverManager().install()
                ),
                options=options
            )

            return driver

        raise Exception("Browser Not Supported")