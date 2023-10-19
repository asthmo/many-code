from selenium.webdriver.common.by import By


class KinopoiskPageLocators:
    INPUT_FILM_TITLE = (By.ID, 'find_film')
    SELECT_COUNTRY = (By.ID, 'country')
    SELECT_GENRE = (By.ID, 'm_act[genre]')
    SET_GENRE = (By.ID, 'm_act[genre_and]')
    SUBMIT = (By.CLASS_NAME, 'nice_button')

    FILM_TITLE = (By.CLASS_NAME, 'name')
