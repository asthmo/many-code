import allure
from Pages.find_page import KinopoiskFindPage


@allure.feature('Kinopoisk Find Film')
class TestFind:

    @allure.title('Search a movie by title')
    def test_find_film(self, driver):
        find_page = KinopoiskFindPage(driver, 'https://www.kinopoisk.ru/s/')
        find_page.open()
        find_page.find_film()
        assert find_page.check_top_five() == True

    @allure.title('Search found film')
    def test_found_film(self, driver):
        find_page = KinopoiskFindPage(driver, 'https://www.kinopoisk.ru/s/')
        find_page.open()
        find_page.find_film()
        assert find_page.check_found_film() == True
