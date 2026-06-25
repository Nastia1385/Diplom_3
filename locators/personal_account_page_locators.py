from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    PROFILE_HEADER = (By.XPATH, "//a[text()='Профиль']")
    HISTORY_ORDERS_BUTTON = (By.XPATH, "//a[contains(@href, '/account/order-history')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")

    # История заказов
    ORDER_HISTORY_ITEM = (By.XPATH,
                          "//li[contains(@class, 'OrderHistory_listItem__2x95r')]//div[contains(@class, 'text_type_digits-default')]")
