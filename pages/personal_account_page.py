from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_order_history(self):
        self.click_element(PersonalAccountPageLocators.HISTORY_ORDERS_BUTTON)

    def click_logout(self):
        self.click_element(PersonalAccountPageLocators.LOGOUT_BUTTON)
