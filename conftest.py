import pytest
import allure
import json
from selenium import webdriver


@pytest.fixture(scope='session')
def config():
    with open('settings.json', 'r', encoding='utf-8') as f:
        settings = json.loads(f.read())
    return settings


@pytest.fixture(scope='session')
def driver(config):
    if config['browser'].lower() == 'chrome':
        driver = webdriver.Chrome()
    elif config['browser'].lower() == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
