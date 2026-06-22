# pages/password_recovery_page.py
from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
import urls


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_password_recovery_page(self):
        self.open_page(urls.PASSWORD_RECOVERY_URL)

    def enter_email_for_recovery(self, email):
        self.send_keys_to_element(PasswordRecoveryPageLocators.EMAIL_INPUT, email)

    def click_recover_button(self):
        self.click_element(PasswordRecoveryPageLocators.RECOVER_BUTTON)

    def show_password(self):
        self.click_element(PasswordRecoveryPageLocators.SHOW_PASSWORD_BUTTON)

    def get_password_input_class(self):
        element = self.find_element(PasswordRecoveryPageLocators.PASSWORD_INPUT)
        return element.get_attribute('class')

    def get_password_input_container_class(self):
        element = self.find_element(PasswordRecoveryPageLocators.PASSWORD_INPUT_CONTAINER)
        return element.get_attribute('class')

    def enter_new_password(self, password):
        self.send_keys_to_element(PasswordRecoveryPageLocators.PASSWORD_INPUT, password)