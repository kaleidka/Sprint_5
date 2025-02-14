import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import EMAIL, MAIN_PAGE, PASSWORD
from locators import Locators as loc

@pytest.fixture
def generate_login():
    random_email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@yandex.ru"
    return random_email

@pytest.fixture
def generate_password():
    random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return random_password

@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument(argument='--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def log_in(driver):
    driver.find_element(*loc.ACCOUNT_LINK).click()
    driver.find_element(*loc.SIGN_IN_EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(*loc.SIGN_IN_PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*loc.SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(loc.BASKET_BUTTON)
    )
