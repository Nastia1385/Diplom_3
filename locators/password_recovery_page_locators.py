# locators/password_recovery_page_locators.py
from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RECOVER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ') and text()='Восстановить']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    PASSWORD_INPUT_CONTAINER = (By.XPATH, "//div[contains(@class, 'input__container')]")