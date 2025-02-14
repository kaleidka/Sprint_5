from locators import Locators as loc
from data import EMAIL, PASSWORD
from base_page import BasePage

class TestSignIn:
    def test_sign_in_with_enter_account_button(self, driver):
        base_page = BasePage(driver)
        button_before = base_page.get_element_text(driver, loc.ENTER_ACCOUNT_BUTTON)
        base_page.click_element(driver, loc.ENTER_ACCOUNT_BUTTON)
        button_after = self._button_after_log_in(driver, base_page)
        assert button_before != button_after

    def test_sign_in_with_account_link(self, driver):
        base_page = BasePage(driver)
        button_before = base_page.get_element_text(driver, loc.ENTER_ACCOUNT_BUTTON)
        base_page.click_element(driver, loc.ACCOUNT_LINK)
        button_after = self._button_after_log_in(driver, base_page)
        assert button_before != button_after

    def test_sign_in_with_link_in_registration_form(self, driver):
        base_page = BasePage(driver)
        button_before = base_page.get_element_text(driver, loc.ENTER_ACCOUNT_BUTTON)
        base_page.click_element(driver, loc.ENTER_ACCOUNT_BUTTON)
        base_page.click_element(driver, loc.SIGN_UP_LINK)
        base_page.click_element(driver, loc.SIGN_IN_LINK)
        button_after = self._button_after_log_in(driver, base_page)
        assert button_before != button_after

    def test_sign_in_with_link_in_restore_password_form(self, driver):
        base_page = BasePage(driver)
        button_before = base_page.get_element_text(driver, loc.ENTER_ACCOUNT_BUTTON)
        base_page.click_element(driver, loc.ENTER_ACCOUNT_BUTTON)
        base_page.click_element(driver, loc.RESTORE_PASSWORD_LINK)
        base_page.click_element(driver, loc.REMEMBER_PASSWORD_SIGN_IN_LINK)
        button_after = self._button_after_log_in(driver, base_page)
        assert button_before != button_after

    def _button_after_log_in(self, driver, base_page):
        base_page.send_keys_to_element(driver, loc.SIGN_IN_EMAIL_INPUT, EMAIL)
        base_page.send_keys_to_element(driver, loc.SIGN_IN_PASSWORD_INPUT, PASSWORD)
        base_page.click_element(driver, loc.SIGN_IN_BUTTON)
        base_page.wait_for_element(driver, loc.BASKET_BUTTON)
        return base_page.get_element_text(driver, loc.BASKET_BUTTON)
