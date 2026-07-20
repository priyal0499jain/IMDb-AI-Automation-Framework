import pytest
import allure
from utilities.logger import get_logger


from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.movie_details_page import MovieDetailsPage
from test_data.movies import movies

logger = get_logger()
@allure.feature("Movie Search")
@pytest.mark.parametrize("search_text, expected_title", movies)
def test_valid_movie_search(driver, search_text, expected_title):

    home = HomePage(driver)
    results = SearchResultsPage(driver)
    movie = MovieDetailsPage(driver)
    

    home.open()
    home.search_movie(search_text)
    results.open_first_movie()

    assert movie.get_title() == expected_title

    logger.info("Opening IMDb")


    logger.info(f"Searching for {search_text}")
    home.search_movie(search_text)

    logger.info("Opening first search result")
    results.open_first_movie()

    logger.info(f"Verified title: {expected_title}")
    assert movie.get_title() == expected_title