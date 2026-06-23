from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RECOVER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ') and text()='Восстановить']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    PASSWORD_INPUT_CONTAINER = (By.XPATH, "//div[contains(@class, 'input__container')]")
    # Контейнер поля ввода пароля (общий)
    PASSWORD_INPUT_CONTAINER = (By.XPATH, "//div[contains(@class, 'input__container')]//input[@name='Введите новый пароль']/parent::div[contains(@class, 'input')]")
    # Контейнер поля ввода пароля (активное состояние - после клика)
    PASSWORD_INPUT_CONTAINER_ACTIVE = (By.XPATH, "//div[contains(@class, 'input__container')]//input[@name='Введите новый пароль']/parent::div[contains(@class, 'input_status_active')]")
    # Сам контейнер целиком
    PASSWORD_CONTAINER_FULL = (By.XPATH, "//div[contains(@class, 'input__container')]")
    # Поле ввода пароля в активном состоянии
    PASSWORD_INPUT_ACTIVE = (By.XPATH, "//input[@name='Введите новый пароль']/parent::div[contains(@class, 'input_status_active')]")