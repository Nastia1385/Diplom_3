from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
import urls
from selenium.webdriver.support import expected_conditions as EC


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_order_feed_page(self):
        self.open_page(urls.ORDER_FEED_URL)

    def get_order_numbers(self):
        elements = self.driver.find_elements(*OrderFeedPageLocators.ORDER_NUMBER_IN_FEED)
        numbers = []
        for element in elements:
            text = element.text
            # Отсеиваем два первых знака # и 0
            if text.startswith('#0'):
                numbers.append(text[2:])
            elif text.startswith('#'):
                numbers.append(text[1:])
            else:
                numbers.append(text)
        return numbers

    # def get_order_numbers(self):
    #     element = self.driver.find_elements(OrderFeedPageLocators.ORDER_NUMBER_IN_FEED)
    #     return element.text

    def click_order_by_number(self, number):
        # Кликаем по заказу с определенным номером
        locator = (By.XPATH,
                   f"//li[contains(@class, 'OrderHistory_listItem__2x95r')]//div[contains(@class, 'text_type_digits-default') and contains(text(), '#{number}')]")
        self.click_element(locator)

    def is_order_details_visible(self):
        return self.find_element(OrderFeedPageLocators.ORDER_DETAILS_MODAL).is_displayed()

    def close_order_details(self):
        self.click_element(OrderFeedPageLocators.ORDER_DETAILS_CLOSE_BUTTON)

    def get_completed_orders_total(self):
        text = self.get_text(OrderFeedPageLocators.ORDERS_COMPLETED_TOTAL)
        return int(text) if text.isdigit() else 0

    def get_completed_orders_today(self):
        text = self.get_text(OrderFeedPageLocators.ORDERS_COMPLETED_TODAY)
        return int(text) if text.isdigit() else 0

    def get_orders_in_progress(self):
        self.wait_for_invisibility(OrderFeedPageLocators.ALL_ORDERS_DONE_MESSAGE, 30)
        elements = self.driver.find_elements(*OrderFeedPageLocators.ORDERS_IN_PROGRESS)
        numbers = []
        for element in elements:
            text = element.text
            # Отсеиваем первый знак 0
            if text.startswith('0'):
                numbers.append(text[1:])
            else:
                numbers.append(text)
        return numbers

    def get_order_detail_number(self):
        element = self.find_element(OrderFeedPageLocators.ORDER_DETAILS_NUMBER)
        text = element.text
        if text.startswith('#'):
            return text[1:]
        return text

    def wait_for_order_in_progress(self, order_number):
        # Ожидаем появления заказа в списке "В работе"
        locator = (By.XPATH,
                   f"//ul[contains(@class, 'OrderFeed_orderListReady__1YFEM')]/li[contains(text(), '{order_number}')]")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(locator)
        )