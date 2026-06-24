from selenium.webdriver.common.by import By


def order_by_number_locator(order_number):
    return By.XPATH, f"//p[contains(@class, 'text_type_digits-default') and text()='#{order_number}']"


class OrderFeedPageLocators:
    ORDER_FEED_HEADER = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]')

    # Список заказов
    ORDER_ITEM = (By.CLASS_NAME, "OrderFeed_list__OLh59")
    ORDER_ITEM_NUMBER = (By.XPATH,
                         "//li[contains(@class, 'OrderHistory_listItem__2x95r')]//div[contains(@class, 'text_type_digits-default')]")
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
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFEM')]/li")
    ORDERS_IN_PROGRESS_LIST = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem .text_type_digits-default")
    ALL_ORDERS_DONE_MESSAGE = (By.XPATH, "//p[text()='Все текущие заказы готовы!']")

    # Номер заказа в оформлении
    ORDER_NUMBER_IN_MODAL = (By.XPATH,
                             "//div[contains(@class, 'Modal_modal__contentBox__sCy8X')]//h2[contains(@class, 'text_type_digits-large')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")
    ORDER_MODAL_CLOSE = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X')]//button[contains(@class, 'Modal_modal__close__TnseK')]")
    ORDER_MODAL_CLOSE_DETAILS = (By.XPATH,
                                 "//section[contains(@class, 'Modal_modal_opened__3ISKW')]//button[contains(@class, 'Modal_modal__close__TnseK')]")
    ORDER_NUMBER_IN_FEED = (By.XPATH, '//p[@class ="text text_type_digits-default"]')

    # Заказ в общем списке
    ORDER_LINK_CLICK = (By.XPATH, "./ancestor::li//a")
