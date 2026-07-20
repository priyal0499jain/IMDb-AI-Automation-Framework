from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MovieDetailsPage(BasePage):

    TITLE = (
        By.XPATH,
        "//h1"
    )

    YEAR = (
        By.XPATH,
        "//a[contains(@href,'releaseinfo')]"
    )

    RATING = (
    By.XPATH,
    "//span[contains(@class,'sc-') and normalize-space()='8.7']"
)

    DURATION = (
        By.XPATH,
        "//li[@data-testid='title-techspec_runtime']//div[contains(@class,'ipc-metadata-list-item__content-container')]"
    )

    DIRECTOR = (
        By.XPATH,
        "//li[@data-testid='title-pc-principal-credit']//a"
    )

    GENRES = (
        By.XPATH,
        "//div[@data-testid='interests']//a"
    )

    STORYLINE = (
        By.XPATH,
        "//span[contains(text(),'Storyline')]"
    )

    CAST = (
        By.XPATH,
        "//a[contains(@href,'/name/')]"
    )

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_release_year(self):
        return self.get_text(self.YEAR)

    def get_rating(self):
        rating = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.RATING)
        )
        return rating.text

    def get_duration(self):
        return self.get_text(self.DURATION)

    def get_director(self):
        return self.get_text(self.DIRECTOR)

    def get_genres(self):
        genres = self.driver.find_elements(*self.GENRES)
        return [genre.text for genre in genres]

    def storyline_displayed(self):
        storyline = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.STORYLINE)
        )
        return storyline.is_displayed()

    def get_cast(self):
        cast = []

        elements = self.driver.find_elements(*self.CAST)

        for element in elements:
            text = element.text.strip()

            if text and text not in cast:
                cast.append(text)

        return cast[:10]