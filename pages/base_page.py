import time

import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        return element

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

    @allure.step('Перетаскивание элемента')
    def drag_and_drop(self, locator_from, locator_to, timeout=10):
        element_from = self.find_element(locator_from, timeout)
        element_to = self.find_element(locator_to, timeout)
        self.driver.execute_script("""
                       var source = arguments[0];
                       var target = arguments[1];
                       var evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       source.dispatchEvent(evt);
                       evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       target.dispatchEvent(evt);
                       evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       target.dispatchEvent(evt);
                       evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       target.dispatchEvent(evt);
                       evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       source.dispatchEvent(evt);
                   """, element_from, element_to)

    def click_element(self, locator, timeout=10):
        time.sleep(0.3)
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def wait_for_text_not_to_be(self, locator, text, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        wait.until_not(EC.text_to_be_present_in_element(locator, text))
        time.sleep(1)

    def open_page(self, url):
        self.driver.get(url)
