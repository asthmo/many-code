import allure
from pages.find_page import KinopoiskFindPage


@allure.feature('Kinopoisk Find Film')
class TestFind:

    @allure.title('Search a movie by title')
    def test_find_film(self, driver):
        find_page = KinopoiskFindPage(driver)
        find_page.set_film()
        find_page.open()
        find_page.find_film()
        assert find_page.check_top_five() == True

    @allure.title('Search found film')
    def test_found_film(self, driver):
        find_page = KinopoiskFindPage(driver)
        find_page.set_film('Место под соснами', 'США', 'драма')
        find_page.open()
        find_page.find_film()
        assert find_page.check_found_film() == True
