from selenium.webdriver.common.by import By


class KinopoiskPageLocators:
    INPUT_FILM_TITLE = (By.XPATH, '//input[@id="find_film"]')
    SELECT_COUNTRY = (By.XPATH, '//select[@id="country"]')
    SELECT_GENRE = (By.XPATH, '//select[@id="m_act[genre]"]')
    SET_GENRE = (By.XPATH, '//input[@id="m_act[genre_and]"]')
    SUBMIT = (By.CSS_SELECTOR, 'form#formSearchMain > input.nice_button')

    FILM_TITLE = (By.CLASS_NAME, 'name')