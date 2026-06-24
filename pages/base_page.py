import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def send_keys_to_element(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text

    def get_attribute(self, locator, attribute, timeout=10):
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)

    def drag_and_drop(self, source_locator, target_locator, timeout=10):
        source = self.find_element(source_locator, timeout)
        target = self.find_element(target_locator, timeout)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def wait_for_invisibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_visibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_text_not_to_be(self, locator, text, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        wait.until_not(EC.text_to_be_present_in_element(locator, text))
        time.sleep(0.5)

    def wait_for_text_to_be(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def open_page(self, url):
        self.driver.get(url)
