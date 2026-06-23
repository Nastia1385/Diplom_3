import urls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.open_page(urls.LOGIN_URL)

    def login(self, email, password):
        self.send_keys_to_element(LoginPageLocators.LOGIN_EMAIL_INPUT, email)
        self.send_keys_to_element(LoginPageLocators.LOGIN_PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def click_password_recovery(self):
        self.click_element(LoginPageLocators.PASSWORD_RECOVERY_LINK)

    def click_register_link(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)
