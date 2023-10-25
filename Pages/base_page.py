from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.kinopoisk.ru/s/'

    def open(self):
        self.driver.get(self.url)

    def get_visible_element(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def get_present_element(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def get_all_present_elements(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)

    def make_screenshot(self):
        self.driver.get_screenshot_as_png()