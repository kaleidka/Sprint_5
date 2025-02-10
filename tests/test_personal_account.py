from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import CONSTRUCTOR_HEADER, PERSONAL_ACCOUNT_TEXT, SIGN_IN_FORM_TITLE
from locators import Locators as loc

class TestPersonalAccount:

    def click_element(self, driver, element_locator):
        driver.find_element(*element_locator).click()

    def wait_for_element(self, driver, element_locator, timeout=5):
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(element_locator)
        )

    def get_element_text(self, driver, element_locator):
        return driver.find_element(*element_locator).text

    def test_enter_account_with_account_link(self, driver, log_in):
        self.click_element(driver, loc.ACCOUNT_LINK)
        self.wait_for_element(driver, loc.PERSONAL_ACCOUNT)
        assert (
            self.get_element_text(driver, loc.PERSONAL_ACCOUNT) ==
            PERSONAL_ACCOUNT_TEXT
        )

    def test_switch_from_account_with_constructor_link(self, driver, log_in):
        self.click_element(driver, loc.ACCOUNT_LINK)
        self.click_element(driver, loc.CONSTRUCTOR_LINK)
        assert (
            self.get_element_text(driver, loc.CONSTRUCT_BURGER) ==
            CONSTRUCTOR_HEADER
        )

    def test_switch_from_account_with_logo_link(self, driver, log_in):
        self.click_element(driver, loc.ACCOUNT_LINK)
        self.click_element(driver, loc.LOGO_LINK)
        assert (
            self.get_element_text(driver, loc.CONSTRUCT_BURGER) ==
            CONSTRUCTOR_HEADER
        )

    def test_log_out_from_account_with_exit_button(self, driver, log_in):
        self.click_element(driver, loc.ACCOUNT_LINK)
        self.wait_for_element(driver, loc.EXIT_BUTTON)
        self.click_element(driver, loc.EXIT_BUTTON)
        self.wait_for_element(driver, loc.SIGN_IN_FORM)
        assert (
            self.get_element_text(driver, loc.SIGN_IN_FORM) ==
            SIGN_IN_FORM_TITLE
        )