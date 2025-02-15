from locators import Locators as loc
from base_page import BasePage

class TestSignIn:
    def test_sign_in_with_enter_account_button(self, driver):
        base_page = BasePage(driver)
        button_before = base_page.get_element_text(driver, loc.ENTER_ACCOUNT_BUTTON)
        base_page.click_element(driver, loc.ENTER_ACCOUNT_BUTTON)
        button_after = base_page.button_after_log_in(driver)
        assert button_before != button_after

    def test_sign_in_with_account_link(self, driver):
        base_page = BasePage(driver)
        button_before = base_page.get_element_text(driver, loc.ENTER_ACCOUNT_BUTTON)
        base_page.click_element(driver, loc.ACCOUNT_LINK)
        button_after = base_page.button_after_log_in(driver)
        assert button_before != button_after

    def test_sign_in_with_link_in_registration_form(self, driver):
        base_page = BasePage(driver)
        button_before = base_page.get_element_text(driver, loc.ENTER_ACCOUNT_BUTTON)
        base_page.click_element(driver, loc.ENTER_ACCOUNT_BUTTON)
        base_page.click_element(driver, loc.SIGN_UP_LINK)
        base_page.click_element(driver, loc.SIGN_IN_LINK)
        button_after = base_page.button_after_log_in(driver)
        assert button_before != button_after

    def test_sign_in_with_link_in_restore_password_form(self, driver):
        base_page = BasePage(driver)
        button_before = base_page.get_element_text(driver, loc.ENTER_ACCOUNT_BUTTON)
        base_page.click_element(driver, loc.ENTER_ACCOUNT_BUTTON)
        base_page.click_element(driver, loc.RESTORE_PASSWORD_LINK)
        base_page.click_element(driver, loc.REMEMBER_PASSWORD_SIGN_IN_LINK)
        button_after = base_page.button_after_log_in(driver)
        assert button_before != button_after
