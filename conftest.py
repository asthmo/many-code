import pytest
import allure
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='session')
def config():
    with open('settings.json', 'r', encoding='utf-8') as f:
        settings = json.loads(f.read())
    return settings


@pytest.fixture(scope='session')
def driver(config):
    if config['browser'].lower() == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
    elif config['browser'].lower() == 'firefox':
        driver = webdriver.Firefox(service=FireFoxService(
            GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
