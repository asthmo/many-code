import allure
import pytest
from framework.ui_pages.search_page import KinopoiskSearchPage
from framework.resources.test_params.film_data import BaseFilm

@pytest.mark.usefixtures('allure_screen')
@allure.feature('Test Kinopoisk Search Film')
class TestKinopoiskSearchFilm:

    @pytest.mark.usefixtures("close_driver_after_test")
    @allure.story('Поиск фильма')
    def test_find_film(self):
        with allure.step('Открываем сайт кинопоиска'):
            search_page = KinopoiskSearchPage().open()

        with allure.step('Заполняем необходимые поля для поиска фильма'):
            search_page.filling_fields(BaseFilm.film_title, BaseFilm.country, BaseFilm.genre)

        with allure.step('Проверяем выданный фильм в поле "Скорее всего вы ищите'):
            search_page.check_most_wanted_film(BaseFilm.film_title)