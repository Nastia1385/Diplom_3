from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки навигации
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href, '/')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@href, '/feed')]")

    # Кнопка для оформления заказа
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ') and text()='Оформить заказ']")
    # Кнопка для входа в аккаунт
    LOG_IN_TO_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Раздел "Соусы"
    SECTION_COUNTS = (By.XPATH, "//span[text()='Соусы']")
    # Раздел начинки
    SECTION_FILLING = (By.XPATH, "//span[text()='Начинки']")
    # Конструктор - ингредиенты
    BUN_INGREDIENT = (By.XPATH, '//a[@href="/ingredient/691577430cc94f001a65b859"]')
    SAUCE_INGREDIENT = (By.XPATH, '//a[@href="/ingredient/691577430cc94f001a65b85f"]')
    FILLING_INGREDIENT = (By.XPATH, '//a[@href="/ingredient/691577430cc94f001a65b866"]')

    # Каунтеры ингредиентов
    BUN_COUNTER = (By.XPATH,
                   "//p[contains(text(),'Краторная булка N-200i')]/ancestor::a//p[@class='counter_counter__num__3nue1']")
    SAUCE_COUNTER = (By.XPATH,
                     "//p[contains(text(),'Соус Spicy-X')]/ancestor::a//p[@class='counter_counter__num__3nue1']")
    FILLING_COUNTER = (By.XPATH,
                       "//p[contains(text(),'Мини-салат Экзо-Плантаго')]/ancestor::a//p[@class='counter_counter__num__3nue1']")

    # Всплывающее окно с деталями ингредиента
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//h2[text()= 'Детали ингредиента']")
    INGREDIENT_DETAILS_MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X')]/h2")

    # Элементы корзины для drag and drop
    BUN_TARGET = (By.XPATH,
                  "//section[contains(@class, 'BurgerConstructor_basket__2jHr3')]//div[contains(@class, 'BurgerConstructor_basket__list__2MXlD')]/div[1]")
    INGREDIENT_TARGET = (By.XPATH,
                         "//section[contains(@class, 'BurgerConstructor_basket__2jHr3')]//ul[contains(@class, 'BurgerConstructor_basket__list__2MXlD')]")
    # Корзина для перетаскивания ингридиентов и булок
    CONSTRUCTOR_BASKET = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]')

    # Заголовок конструктора для проверки
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

    PULL_THE_BUN_UP = (By.XPATH, "//span[text()='Перетяните булочку сюда (верх)']")
    PULL_THE_BUN_DOWN = (By.XPATH, "//span[text()='Перетяните булочку сюда (низ)']")

    ORDER_NUMBER_IN_MODAL = (By.XPATH, '// h2[@class ="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    ORDER_MODAL_CLOSE_DETAILS = (By.XPATH, '')