from selenium.webdriver.common.by import By


def order_by_number_locator(order_number):
    return By.XPATH, f"//p[contains(@class, 'text_type_digits-default') and text()='#{order_number}']"


class OrderFeedPageLocators:
    # Список заказов
    ORDER_ITEM = (By.CLASS_NAME, "OrderFeed_list__OLh59")
    ORDER_ELEMENTS = (By.CSS_SELECTOR, ".text_type_digits-default")

    # Детали заказа в модальном окне
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi')]")
    ORDER_DETAILS_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
    ORDER_DETAILS_NUMBER = (By.XPATH,
                            "//div[contains(@class, 'Modal_modal__contentBox__sCy8X')]//h2[contains(@class, 'text_type_digits-default')]")

    # Статистика заказов
    ORDERS_COMPLETED_TOTAL = (By.XPATH,
                              '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "OrderFeed_number__2MbrQ")]')
    ORDERS_COMPLETED_TODAY = (By.XPATH,
                              "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")

    # Список заказов в работе
    ORDERS_IN_PROGRESS_LIST = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem .text_type_digits-default")

    # Заказ в общем списке
    ORDER_LINK_CLICK = (By.XPATH, "./ancestor::li//a")
