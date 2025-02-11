from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import EMAIL, PASSWORD
from locators import Locators as loc

class TestSignIn:

    def click_element(self, driver, element_locator):
        driver.find_element(*element_locator).click()

    def send_keys_to_element(self, driver, element_locator, keys):
        driver.find_element(*element_locator).send_keys(keys)

    def wait_for_element(self, driver, element_locator, timeout=5):
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(element_locator)
        )

    def button_after_log_in(self, driver):
        self.send_keys_to_element(driver, loc.SIGN_IN_EMAIL_INPUT, EMAIL)
        self.send_keys_to_element(driver, loc.SIGN_IN_PASSWORD_INPUT, PASSWORD)
        self.click_element(driver, loc.SIGN_IN_BUTTON)
        self.wait_for_element(driver, loc.BASKET_BUTTON)
        return driver.find_element(*loc.BASKET_BUTTON).text

    def get_button_text(self, driver, element_locator):
        return driver.find_element(*element_locator).text

    def test_sign_in_with_enter_account_button(self, driver):
        button_before = self.get_button_text(driver, loc.ENTER_ACCOUNT_BUTTON)
        self.click_element(driver, loc.ENTER_ACCOUNT_BUTTON)
        assert button_before != self.button_after_log_in(driver)

    def test_sign_in_with_account_link(self, driver):
        button_before = self.get_button_text(driver, loc.ENTER_ACCOUNT_BUTTON)
        self.click_element(driver, loc.ACCOUNT_LINK)
        assert button_before != self.button_after_log_in(driver)

    def test_sign_in_with_link_in_registration_form(self, driver):
        button_before = self.get_button_text(driver, loc.ENTER_ACCOUNT_BUTTON)
        self.click_element(driver, loc.ENTER_ACCOUNT_BUTTON)
        self.click_element(driver, loc.SIGN_UP_LINK)
        self.click_element(driver, loc.SIGN_IN_LINK)
        assert button_before != self.button_after_log_in(driver)

    def test_sign_in_with_link_in_restore_password_form(self, driver):
        button_before = self.get_button_text(driver, loc.ENTER_ACCOUNT_BUTTON)
        self.click_element(driver, loc.ENTER_ACCOUNT_BUTTON)
        self.click_element(driver, loc.RESTORE_PASSWORD_LINK)
        self.click_element(driver, loc.REMEMBER_PASSWORD_SIGN_IN_LINK)
        assert button_before != self.button_after_log_in(driver)