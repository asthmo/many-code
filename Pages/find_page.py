import json
import allure
from allure_commons.types import AttachmentType
from Locators.kinopoisk_page_locators import KinopoiskPageLocators
from Pages.base_page import BasePage


class KinopoiskFindPage(BasePage):
    locators = KinopoiskPageLocators()
    with open('settings.json', 'r', encoding='utf-8') as f:
        settings = json.loads(f.read())

    @allure.step('Fill fields and submit')
    def find_film(self):
        with allure.step('Filling fields'):
            self.elements_is_visible(self.locators.INPUT_FILM_TITLE).send_keys(
                self.settings['film']['title'])
            self.elements_is_visible(self.locators.SELECT_COUNTRY).send_keys(
                self.settings['film']['country'])
            self.elements_is_visible(self.locators.SELECT_GENRE).send_keys(
                self.settings['film']['genre'])
            self.elements_is_present(self.locators.SET_GENRE).click()
            allure.attach(self.driver.get_screenshot_as_png(),
                          'screenshot', AttachmentType.PNG)
        with allure.step('Click submit'):
            self.elements_is_present(self.locators.SUBMIT).click()

    @allure.step('Check film in top five')
    def check_top_five(self):
        with allure.step('Getting a list of top 5 films'):
            name_list = self.elements_are_present(self.locators.FILM_TITLE)
            allure.attach(self.driver.get_screenshot_as_png(),
                          'screenshot', AttachmentType.PNG)
        with allure.step('Checking for a movie in the top 5'):
            for element in range(1, 6):
                if self.settings['film']['title'] == name_list[element].text:
                    return True
            return False

    @allure.step('Check found film')
    def check_found_film(self):
        with allure.step('Getting a movie from a more similar one'):
            film_name = self.elements_are_present(self.locators.FILM_TITLE)[0]
            allure.attach(self.driver.get_screenshot_as_png(),
                          'screenshot', AttachmentType.PNG)
        with allure.step('Checking the match of the found film'):
            if self.settings['film']['title'] in film_name.text:
                return True
            return False
