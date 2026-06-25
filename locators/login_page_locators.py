from selenium.webdriver.common.by import By

class LoginPageLocators:
    # LOGIN_NAME_INPUT = (By.XPATH, "//label[text()='Имя']")
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ') and text()='Войти']")
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[contains(@href, '/forgot-password')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(@href, '/register')]")