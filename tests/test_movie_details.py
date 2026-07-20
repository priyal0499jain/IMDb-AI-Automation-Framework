import allure

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.movie_details_page import MovieDetailsPage


@allure.feature("Movie Details")
@allure.story("Verify movie information")
@allure.title("Verify Interstellar details")
@allure.description("Opens Interstellar and validates title, year, rating, duration, director, genres and storyline.")
def test_movie_details(driver):

    home = HomePage(driver)
    results = SearchResultsPage(driver)
    movie = MovieDetailsPage(driver)

    home.open()
    home.search_movie("Interstellar")
    results.open_first_movie()

    assert movie.get_title() == "Interstellar"

    print("Movie Title :", movie.get_title())
    print("Release Year :", movie.get_release_year())
    print("IMDb Rating :", movie.get_rating())
    print("Duration :", movie.get_duration())
    print("Director :", movie.get_director())
    print("Genres :", movie.get_genres())

    assert movie.storyline_displayed()