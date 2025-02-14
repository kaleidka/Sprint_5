from base_page import BasePage
from locators import Locators as loc

class TestConstructor:
    def test_switch_to_buns_in_constructor(self, driver):
        base_page = BasePage(driver)
        base_page.click_element(driver, loc.SAUCES)
        base_page.click_element(driver, loc.BUNS)
        base_page.check_active_category(driver, loc.BUNS, [loc.TOPPINGS, loc.SAUCES])

    def test_switch_to_sauces_in_constructor(self, driver):
        base_page = BasePage(driver)
        base_page.click_element(driver, loc.SAUCES)
        base_page.check_active_category(driver, loc.SAUCES, [loc.BUNS, loc.TOPPINGS])

    def test_switch_to_toppings_in_constructor(self, driver):
        base_page = BasePage(driver)
        base_page.click_element(driver, loc.TOPPINGS)
        base_page.check_active_category(driver, loc.TOPPINGS, [loc.BUNS, loc.SAUCES])
