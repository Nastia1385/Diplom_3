import urls
from locators.order_feed_page_locators import OrderFeedPageLocators, order_by_number_locator
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_order_feed_page(self):
        self.open_page(urls.ORDER_FEED_URL)

    def get_order_numbers(self):
        order_list = self.find_element(OrderFeedPageLocators.ORDER_ITEM)
        order_elements = order_list.find_elements(*OrderFeedPageLocators.ORDER_ELEMENTS)
        order_numbers = [el.text.replace('#', '') for el in order_elements]
        return order_numbers

    def click_order_by_number(self, order_number):
        # Кликаем по заказу с определенным номером
        order_element = self.find_element(order_by_number_locator(order_number))
        link = order_element.find_element(*OrderFeedPageLocators.ORDER_LINK_CLICK)
        link.click()

    def is_order_details_visible(self):
        return self.find_element(OrderFeedPageLocators.ORDER_DETAILS_MODAL).is_displayed()

    def get_completed_orders_total(self):
        text = self.get_text(OrderFeedPageLocators.ORDERS_COMPLETED_TOTAL)
        return int(text) if text.isdigit() else 0

    def get_completed_orders_today(self):
        text = self.get_text(OrderFeedPageLocators.ORDERS_COMPLETED_TODAY)
        return int(text) if text.isdigit() else 0

    def get_orders_in_progress(self):
        # Ждем появления хотя бы одного элемента
        order_elements = self.find_elements(OrderFeedPageLocators.ORDERS_IN_PROGRESS_LIST)
        order_numbers = [el.text for el in order_elements]
        return order_numbers
