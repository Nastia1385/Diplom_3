import allure


class TestMainFunctionality:

    @allure.title("Переход на главную страницу по клику на «Конструктор»")
    def test_click_constructor_redirects_to_main(self, driver, main_page, login_page, user):
        with allure.step("Логинимся"):
            login_page.open_login_page()
            login_page.login(user['email'], user['password'])

        with allure.step("Переходим в личный кабинет"):
            main_page.click_personal_account()

        with allure.step("Кликаем на «Конструктор»"):
            main_page.click_constructor()

        with allure.step("Проверяем, что находимся на главной странице"):
            assert "/" in main_page.current_url()
            assert main_page.is_constructor_title_visible()

    @allure.title("Переход на страницу «Лента заказов»")
    def test_click_order_feed_redirects_to_feed(self, driver, main_page, login_page, user):
        with allure.step("Логинимся"):
            login_page.open_login_page()
            login_page.login(user['email'], user['password'])

        with allure.step("Кликаем на «Ленту заказов»"):
            main_page.click_order_feed()

        with allure.step("Проверяем, что перешли на страницу ленты заказов"):
            assert "/feed" in main_page.current_url()

    @allure.title("Открытие модального окна с деталями ингредиента")
    def test_click_ingredient_shows_details_modal(self, driver, main_page):
        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()

        with allure.step("Кликаем на ингредиент (булка)"):
            main_page.click_bun_ingredient()

        with allure.step("Проверяем, что появилось модальное окно"):
            assert main_page.is_ingredient_details_visible()

    @allure.title("Закрытие модального окна деталей ингредиента")
    def test_close_ingredient_details_modal(self, driver, main_page):
        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()

        with allure.step("Открываем детали ингредиента"):
            main_page.click_bun_ingredient()

        with allure.step("Закрываем модальное окно крестиком"):
            main_page.close_ingredient_details()

        with allure.step("Ожидаем исчезновения модального окна"):
            main_page.check_invisibility_ingredient_details_modal()

        with allure.step("Проверяем, что модальное окно закрылось"):
            assert not main_page.is_ingredient_details_visible(), "Модальное окно деталей ингредиента не закрылось"

    @allure.title("Увеличение каунтера булки на 2 при добавлении в заказ")
    def test_add_bun_increases_counter_by_2(self, driver, main_page):
        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()

        with allure.step("Получаем начальное значение каунтера булки"):
            initial_counter = main_page.get_bun_counter()

        with allure.step("Добавляем булку в заказ"):
            main_page.add_bun_to_order()

        with allure.step("Получаем новое значение каунтера булки"):
            new_counter = main_page.get_bun_counter()

        with allure.step("Проверяем, что каунтер увеличился на 2"):
            assert new_counter == initial_counter + 2

    @allure.title("Увеличение каунтера ингредиента на 1 при добавлении в заказ")
    def test_add_ingredient_increases_counter_by_1(self, driver, main_page):
        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()

        with allure.step("Получаем начальное значение каунтера соуса"):
            initial_counter = main_page.get_sauce_counter()

        with allure.step("Добавляем ингредиент в заказ"):
            main_page.add_ingredient_to_order()

        with allure.step("Получаем новое значение каунтера соуса"):
            new_counter = main_page.get_sauce_counter()

        with allure.step("Проверяем, что каунтер увеличился на 1"):
            assert new_counter == initial_counter + 1

    @allure.title("Создание заказа авторизованным пользователем")
    def test_logged_in_user_can_create_order(self, driver, main_page, login_page, user):
        with allure.step("Логинимся"):
            login_page.open_login_page()
            login_page.login(user['email'], user['password'])

        with allure.step("Добавляем ингредиент в заказ"):
            main_page.add_ingredient_to_order()

        with allure.step("Добавляем булку в заказ"):
            main_page.add_bun_to_order()

        with allure.step("Нажимаем кнопку оформления заказа"):
            main_page.click_order_button()

        with allure.step("Ожидаем появления номера заказа (не 9999)"):
            order_number = main_page.wait_for_order_number_not_9999()

        with allure.step("Проверяем, что номер заказа получен и корректен"):
            assert (order_number is not None
                    and order_number != "9999"
                    and order_number.isdigit())