from data import INVALID_PASSWORD, USER_NAME, WARNING
from locators import Locators as loc
from base_page import BasePage

class TestRegistration(BasePage):

    def test_sign_up_new_account_created(self, driver, generate_login, generate_password):
        self.click_element(driver, loc.ENTER_ACCOUNT_BUTTON)
        self.click_element(driver, loc.SIGN_UP_LINK)
        self.send_keys_to_element(driver, loc.SIGN_UP_NAME_INPUT, USER_NAME)
        self.send_keys_to_element(driver, loc.SIGN_UP_EMAIL_INPUT, generate_login)
        self.send_keys_to_element(driver, loc.SIGN_UP_PASSWORD_INPUT, generate_password)
        self.click_element(driver, loc.SIGN_UP_BUTTON)
        self.click_element(driver, loc.ACCOUNT_LINK)
        self.send_keys_to_element(driver, loc.SIGN_IN_EMAIL_INPUT, generate_login)
        self.send_keys_to_element(driver, loc.SIGN_IN_PASSWORD_INPUT, generate_password)
        self.click_element(driver, loc.SIGN_IN_BUTTON)
        self.wait_for_element(driver, loc.BASKET_BUTTON)
        self.click_element(driver, loc.ACCOUNT_LINK)
        self.wait_for_element(driver, loc.PROFILE_LINK)
        self.click_element(driver, loc.PROFILE_LINK)
        assert (
            driver.find_element(*loc.PROFILE_NAME).get_attribute('value') == USER_NAME and
            driver.find_element(*loc.PROFILE_LOGIN).get_attribute('value') == generate_login
        )

    def test_sign_up_with_invalid_password_warning(self, driver):
        self.click_element(driver, loc.ENTER_ACCOUNT_BUTTON)
        self.click_element(driver, loc.SIGN_UP_LINK)
        self.send_keys_to_element(driver, loc.SIGN_UP_PASSWORD_INPUT, INVALID_PASSWORD)
        self.click_element(driver, loc.SIGN_UP_BUTTON)
        assert driver.find_element(*loc.INVALID_PASSWORD_WARNING).text == WARNING