import json
import allure
from allure_commons.types import AttachmentType
from locators.kinopoisk_page_locators import KinopoiskPageLocators
from pages.base_page import BasePage
import time


class KinopoiskFindPage(BasePage):
    locators = KinopoiskPageLocators()
    def set_film(self, title = '', country = '', genre = ''):
        if title == '':
            with open('settings.json', 'r', encoding='utf-8') as f:
                self.settings = json.loads(f.read())
                self.title = self.settings['film']['title']
                self.country = self.settings['film']['country']
                self.genre = self.settings['film']['genre']
        else:
            self.title = title
            self.country = country
            self.genre = genre

    @allure.step('Fill fields and submit')
    def find_film(self):
        with allure.step('Filling fields'):
            self.get_visible_element(self.locators.INPUT_FILM_TITLE).send_keys(
                self.title)
            self.get_visible_element(self.locators.SELECT_COUNTRY).send_keys(
                self.country)

            self.get_visible_element(self.locators.SELECT_GENRE).send_keys(self.genre)
            self.get_present_element(self.locators.SET_GENRE).click()
            
            allure.attach(self.driver.get_screenshot_as_png(),
                          'screenshot', AttachmentType.PNG)
        with allure.step('Click submit'):
            self.get_present_element(self.locators.SUBMIT).click()

    @allure.step('Check film in top five')
    def check_top_five(self):
        with allure.step('Getting a list of top 5 films'):
            names_list = self.get_all_present_elements(self.locators.FILM_TITLE)
            allure.attach(self.driver.get_screenshot_as_png(),
                          'screenshot', AttachmentType.PNG)
        with allure.step('Checking for a movie in the top 5'):
            for element in names_list[:5]:
                if self.settings['film']['title'] == element.text:
                    return True
            return False

    @allure.step('Check found film')
    def check_found_film(self):
        with allure.step('Getting a movie from a more similar one'):
            film_name = self.get_present_element(self.locators.FILM_TITLE)
            allure.attach(self.driver.get_screenshot_as_png(),
                          'screenshot', AttachmentType.PNG)
        with allure.step('Checking the match of the found film'):
            if self.title in film_name.text:
                return True
            return False
