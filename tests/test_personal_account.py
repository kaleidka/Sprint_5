from data import CONSTRUCTOR_HEADER, PERSONAL_ACCOUNT_TEXT, SIGN_IN_FORM_TITLE
from locators import Locators as loc
from base_page import BasePage

class TestPersonalAccount:
    def test_enter_account_with_account_link(self, driver, log_in):
        base_page = BasePage(driver)
        base_page.click_element(driver, loc.ACCOUNT_LINK)
        base_page.wait_for_element(driver, loc.PERSONAL_ACCOUNT)
        assert (
            base_page.get_element_text(driver, loc.PERSONAL_ACCOUNT) ==
            PERSONAL_ACCOUNT_TEXT
        )

    def test_switch_from_account_with_constructor_link(self, driver, log_in):
        base_page = BasePage(driver)
        base_page.click_element(driver, loc.ACCOUNT_LINK)
        base_page.click_element(driver, loc.CONSTRUCTOR_LINK)
        assert (
            base_page.get_element_text(driver, loc.CONSTRUCT_BURGER) ==
            CONSTRUCTOR_HEADER
        )

    def test_switch_from_account_with_logo_link(self, driver, log_in):
        base_page = BasePage(driver)
        base_page.click_element(driver, loc.ACCOUNT_LINK)
        base_page.click_element(driver, loc.LOGO_LINK)
        assert (
            base_page.get_element_text(driver, loc.CONSTRUCT_BURGER) ==
            CONSTRUCTOR_HEADER
        )

    def test_log_out_from_account_with_exit_button(self, driver, log_in):
        base_page = BasePage(driver)
        base_page.click_element(driver, loc.ACCOUNT_LINK)
        base_page.wait_for_element(driver, loc.EXIT_BUTTON)
        base_page.click_element(driver, loc.EXIT_BUTTON)
        base_page.wait_for_element(driver, loc.SIGN_IN_FORM)
        assert (
            base_page.get_element_text(driver, loc.SIGN_IN_FORM) ==
            SIGN_IN_FORM_TITLE
        )
