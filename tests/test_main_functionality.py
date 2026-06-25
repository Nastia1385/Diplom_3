import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators

class TestMainFunctionality:

    @allure.step
    def test_click_constructor_redirects_to_main(self, driver, main_page, login_page, user):
        """Проверка перехода по клику на «Конструктор»"""
        # Логинимся
        login_page.open_login_page()
        login_page.login(user['email'], user['password'])
        # Переходим в личный кабинет
        main_page.click_personal_account()
        # Кликаем на Конструктор
        main_page.click_constructor()
        # Проверяем, что на главной странице
        assert "/" in driver.current_url
        assert main_page.is_constructor_title_visible()

    @allure.step
    def test_click_order_feed_redirects_to_feed(self, driver, main_page, login_page, user):
        """Проверка перехода по клику на «Лента заказов»"""
        # Логинимся
        login_page.open_login_page()
        login_page.login(user['email'], user['password'])
        # Кликаем на Ленту заказов
        main_page.click_order_feed()
        # Проверяем, что перешли на страницу ленты заказов
        assert "/feed" in driver.current_url

    @allure.step
    def test_click_ingredient_shows_details_modal(self, driver, main_page):
        """Проверка появления всплывающего окна с деталями при клике на ингредиент"""
        main_page.open_main_page()
        # Кликаем на ингредиент
        main_page.click_bun_ingredient()
        # Проверяем, что появилось модальное окно
        assert main_page.is_ingredient_details_visible()


    @allure.step
    def test_close_ingredient_details_modal(self, driver, main_page):
        """Проверка закрытия всплывающего окна кликом по крестику"""
        main_page.open_main_page()
        # Открываем детали ингредиента
        main_page.click_bun_ingredient()
        # Закрываем модальное окно
        main_page.close_ingredient_details()
        # Проверяем, что модальное окно закрылось (дожидаемся исчезновения)
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS_MODAL)
        )
        assert not main_page.is_ingredient_details_visible(), "Модальное окно деталей ингредиента не закрылось"

    @allure.step
    def test_add_bun_increases_counter_by_2(self, driver, main_page):
        """Проверка увеличения каунтера булки на 2 при добавлении в заказ"""
        main_page.open_main_page()
        # Получаем начальное значение каунтера булки
        initial_counter = main_page.get_bun_counter()
        # Добавляем булку
        main_page.add_bun_to_order()
        # Получаем новое значение каунтера булки
        new_counter = main_page.get_bun_counter()
        # Проверяем, что каунтер увеличился на 2
        assert new_counter == initial_counter + 2

    @allure.step
    def test_add_ingredient_increases_counter_by_1(self, driver, main_page):
        """Проверка увеличения каунтера ингредиента на 1 при добавлении в заказ"""
        main_page.open_main_page()
        # Получаем начальное значение каунтера соуса
        initial_counter = main_page.get_sauce_counter()
        # Добавляем ингредиент
        main_page.add_ingredient_to_order()
        # Получаем новое значение каунтера соуса
        new_counter = main_page.get_sauce_counter()
        # Проверяем, что каунтер увеличился на 1
        assert new_counter == initial_counter + 1


# # TODO работает не стабильно
#     @allure.step
#     def test_logged_in_user_can_create_order(self, driver, main_page, login_page, user):
#         """Проверка создания заказа залогиненным пользователем"""
#         # Логинимся
#         login_page.open_login_page()
#         login_page.login(user['email'], user['password'])
#
#         # Добавляем булку и ингредиент в заказ
#         main_page.add_ingredient_to_order()
#         main_page.add_bun_to_order()
#
#         # Нажимаем на кнопку оформления заказа
#         main_page.click_order_button()
#
#         # Ожидаем появления номера заказа (текст не должен быть 9999)
#         order_number = main_page.wait_for_order_number_not_9999()
#
#         # Проверяем, что номер заказа получен
#         assert order_number is not None
#         assert order_number != "9999"
#         assert order_number.isdigit()
#
