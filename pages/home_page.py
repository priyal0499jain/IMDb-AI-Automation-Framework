from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time


class HomePage(BasePage):

    SEARCH_BOX = (By.NAME, "q")

    def open(self):
        self.driver.get("https://www.imdb.com")

    def search_movie(self, movie_name):
        element = self.find_element(self.SEARCH_BOX)

       

        element.clear()

        element.send_keys(movie_name)

        

        time.sleep(2)

        element.send_keys(Keys.ENTER)

       

        time.sleep(5)

        