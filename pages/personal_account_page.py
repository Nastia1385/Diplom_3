# pages/personal_account_page.py
from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators
import urls


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_account_page(self):
        self.open_page(urls.ACCOUNT_URL)

    def click_order_history(self):
        self.click_element(PersonalAccountPageLocators.HISTORY_ORDERS_BUTTON)

    def click_logout(self):
        self.click_element(PersonalAccountPageLocators.LOGOUT_BUTTON)

    def get_order_history_numbers(self):
        elements = self.driver.find_elements(*PersonalAccountPageLocators.ORDER_HISTORY_ITEM)
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

    def is_profile_header_visible(self):
        return self.find_element(PersonalAccountPageLocators.PROFILE_HEADER).is_displayed()