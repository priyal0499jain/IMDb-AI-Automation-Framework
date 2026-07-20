from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    FIRST_MOVIE = (
    By.XPATH,
    "(//a[contains(@href,'/title/')])[1]"
    )
    

    def open_first_movie(self):
        self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//a[contains(@href,'/title/')]")
            )
        )

        movies = self.driver.find_elements(
            By.XPATH,
            "//a[contains(@href,'/title/')]"
        )

        for movie in movies:
            text = movie.text

            if text.strip():
                movie.click()
                return

        raise Exception("No movie link found.")

    def is_first_movie_displayed(self):
        return self.is_displayed(self.FIRST_MOVIE)