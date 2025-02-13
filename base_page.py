from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import ACTIVE
from locators import Locators as loc

class BasePage:
    def click_element(self, driver, element_locator):
        driver.find_element(*element_locator).click()

    def send_keys_to_element(self, driver, element_locator, keys):
        driver.find_element(*element_locator).send_keys(keys)

    def wait_for_element(self, driver, element_locator, timeout=5):
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(element_locator)
        )

    def get_element_text(self, driver, element_locator):
        return driver.find_element(*element_locator).text

    def get_element_attribute(self, driver, element_locator, attribute):
        return driver.find_element(*element_locator).get_attribute(attribute)

    def check_active_category(self, driver, active_locator, inactive_locators):
        active_class = self.get_element_attribute(driver, active_locator, 'class')
        assert ACTIVE in active_class

        for locator in inactive_locators:
            inactive_class = self.get_element_attribute(driver, locator, 'class')
            assert ACTIVE not in inactive_class