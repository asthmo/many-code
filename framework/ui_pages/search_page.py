import json
from selene.browser import open_url
from selene.support.conditions import be
from selene.support.jquery_style_selectors import s, ss
from selene.api import *
from selenium.webdriver.support import select

class KinopoiskSearchPage:
    def __init__(self):
        self.input_film_title = s('input#find_film')
        self.select_country = s('select#country')
        self.select_genre = s('select#m_act[genre]')
        self.submit = s('input.nice_button')

    def open(self):
        open_url('/')
        return self

    def filling_fields(self, title, country, genre):
        self.input_film_title.set(title)
        self.select_country.scroll_to()
        self.select_country.send_keys(country)
        # self.select_genre.all('option').element_by(have.text(genre))

        self.submit.click()
        return self

    def check_most_wanted_film(self, title):
        s('div.most_wanted').s('p.name').should(have.text(title))
