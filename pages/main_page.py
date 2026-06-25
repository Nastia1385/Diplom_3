import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.open_page(urls.MAIN_PAGE_URL)

    def click_personal_account(self):
        # Ждем появления элемента
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )

        # Ждем, пока элемент станет кликабельным
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )

        # Скроллим до элемента
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)

        # Кликаем обычным способом
        element.click()

    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    def click_bun_ingredient(self):
        self.click_element(MainPageLocators.BUN_INGREDIENT)

    # def click_sauce_ingredient(self):
    #     self.click_element(MainPageLocators.SAUCE_INGREDIENT)

    def click_filling_ingredient(self):
        self.click_element(MainPageLocators.FILLING_INGREDIENT)

    def close_ingredient_details(self):
        self.click_element(MainPageLocators.INGREDIENT_DETAILS_MODAL_CLOSE_BUTTON)

    def is_ingredient_details_visible(self):
        return self.find_element(MainPageLocators.INGREDIENT_DETAILS_MODAL).is_displayed()

    def get_bun_counter(self):
        count = self.driver.find_element(*MainPageLocators.BUN_COUNTER)
        return int(count.text)

    def get_sauce_counter(self):
        count = self.driver.find_element(*MainPageLocators.SAUCE_COUNTER)
        return int(count.text)

    # def get_filling_counter(self):
    #     count = self.driver.find_element(*MainPageLocators.FILLING_COUNTER)
    #     return int(count.text)

    def add_bun_to_order(self):
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.PULL_THE_BUN_UP)

    def add_ingredient_to_order(self):
        # Добавляем любой ингредиент (соус или начинку)
        self.drag_and_drop(MainPageLocators.SAUCE_INGREDIENT, MainPageLocators.PULL_THE_BUN_UP)

    def is_constructor_title_visible(self):
        return self.find_element(MainPageLocators.CONSTRUCTOR_TITLE).is_displayed()

    def wait_for_order_number_not_9999(self):
        # Ожидание пока текст на элементе не перестанет быть равным 9999
        self.wait_for_text_not_to_be(MainPageLocators.ORDER_NUMBER_IN_MODAL, "9999")
        # Получаем номер заказа
        order_number_element = self.find_element(MainPageLocators.ORDER_NUMBER_IN_MODAL)
        return order_number_element.text

    def close_order_modal(self):
        # Используем локатор, который ниже по дереву
        self.click_element(MainPageLocators.ORDER_MODAL_CLOSE_DETAILS)
