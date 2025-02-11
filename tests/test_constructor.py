from base_page import BasePage
from locators import Locators as loc

class TestConstructor(BasePage):
    def test_switch_to_buns_in_constructor(self, driver):
        self.click_element(driver, loc.SAUCES)
        self.click_element(driver, loc.BUNS)
        self.check_active_category(driver, loc.BUNS, [loc.TOPPINGS, loc.SAUCES])

    def test_switch_to_sauces_in_constructor(self, driver):
        self.click_element(driver, loc.SAUCES)
        self.check_active_category(driver, loc.SAUCES, [loc.BUNS, loc.TOPPINGS])

    def test_switch_to_toppings_in_constructor(self, driver):
        self.click_element(driver, loc.TOPPINGS)
        self.check_active_category(driver, loc.TOPPINGS, [loc.BUNS, loc.SAUCES])