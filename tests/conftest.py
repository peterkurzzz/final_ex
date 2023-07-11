import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#   адрес тестовой страницы
BASE_URL = 'https://b2c.passport.rt.ru'

#   Абсолютный путь к драйверу chrome
s = Service('/home/kurz/PycharmProjects/final_exam/src/driver/chromedriver')


@pytest.fixture(scope="session")
def browser():
    print('запуск GoogleChrome')
    browser = webdriver.Chrome(service=s)
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get(BASE_URL)

    yield browser

    print('конец сессии')
    browser.quit()


@pytest.fixture(scope="session")
def browser_reg_page():
    browser = webdriver.Chrome(service=s)
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get(BASE_URL)
    browser.find_element(By.ID, 'kc-register').click()

    yield browser

    print('конец сессии')
    browser.quit()
