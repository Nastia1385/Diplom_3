import allure
import pytest

from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.title("Проверка открытия всплывающего окна с деталями при клике на заказ в ленте")
    @allure.step("Тест: клик по заказу в ленте открывает детали")
    def test_click_order_in_feed_opens_details(self, driver, order_feed_page):
        with allure.step("Открыть страницу ленты заказов"):
            order_feed_page.open_order_feed_page()

        with allure.step("Получить номера заказов из ленты"):
            order_feed_page = OrderFeedPage(driver)
            order_numbers = order_feed_page.get_order_numbers()

        with allure.step(f"Кликнуть по первому заказу (номер {order_numbers[0]})"):
            order_feed_page.click_order_by_number(order_numbers[0])

        with allure.step("Проверить, что открылось модальное окно с деталями заказа"):
            assert order_feed_page.is_order_details_visible()

    @allure.title("Проверка отображения заказов пользователя на странице Лента заказов")
    @allure.step("Тест: отображение заказов пользователя в ленте")
    def test_user_orders_visible_in_order_feed(self, driver, main_page, login_page, user):
        with allure.step("Авторизоваться под пользователем"):
            login_page.open_login_page()
            login_page.login(user['email'], user['password'])

        with allure.step("Создать новый заказ"):
            main_page.add_ingredient_to_order()
            main_page.add_bun_to_order()
            main_page.click_order_button()
            order_number = int(main_page.wait_for_order_number_not_9999())
            main_page.close_order_modal()

        with allure.step("Перейти в ленту заказов"):
            main_page.click_order_feed()

        with allure.step(f"Получить номера заказов из ленты и проверить наличие созданного заказа #{order_number}"):
            order_feed_page = OrderFeedPage(driver)
            feed_order_numbers = order_feed_page.get_order_numbers()
            assert order_number in [int(num) for num in feed_order_numbers]

    @pytest.mark.parametrize("counter_method, counter_name", [
        ("get_completed_orders_total", "за всё время"),
        ("get_completed_orders_today", "за сегодня")
    ])
    @allure.title("Проверка увеличения счетчиков 'Выполнено за всё время' и 'Выполнено за сегодня' при создании заказа")
    @allure.step("Тест: создание заказа увеличивает счетчики выполненных заказов")
    def test_create_order_increases_completed_counters(self, driver, main_page, login_page, user, counter_method,
                                                       counter_name):
        with allure.step("Авторизоваться под пользователем"):
            login_page.open_login_page()
            login_page.login(user['email'], user['password'])

        with allure.step(f"Перейти в ленту заказов и получить начальное значение счетчика '{counter_name}'"):
            main_page.click_order_feed()
            order_feed_page = OrderFeedPage(driver)
            get_counter = getattr(order_feed_page, counter_method)
            initial_value = get_counter()

        with allure.step("Вернуться на главную и создать новый заказ"):
            main_page.click_constructor()
            main_page.add_ingredient_to_order()
            main_page.add_bun_to_order()
            main_page.click_order_button()
            main_page.wait_for_order_number_not_9999()
            main_page.close_order_modal()

        with allure.step(f"Перейти в ленту заказов и получить новое значение счетчика '{counter_name}'"):
            main_page.click_order_feed()
            new_value = get_counter()

        with allure.step(f"Проверить, что счетчик 'Выполнено {counter_name}' увеличился"):
            assert new_value > initial_value, f"Счетчик 'Выполнено {counter_name}' не увеличился после создания заказа"

    @allure.title("Проверка появления номера заказа в разделе 'В работе' после оформления")
    @allure.step("Тест: номер заказа появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress_after_creation(self, driver, main_page, login_page, user):
        with allure.step("Авторизоваться под пользователем"):
            login_page.open_login_page()
            login_page.login(user['email'], user['password'])

        with allure.step("Создать новый заказ"):
            main_page.add_ingredient_to_order()
            main_page.add_bun_to_order()
            main_page.click_order_button()
            order_number = main_page.wait_for_order_number_not_9999()
            main_page.close_order_modal()

        with allure.step("Перейти в ленту заказов"):
            main_page.click_order_feed()

        with allure.step(f"Получить заказы в работе и проверить наличие заказа #{order_number}"):
            order_feed_page = OrderFeedPage(driver)
            order_numbers_in_progress = order_feed_page.get_orders_in_progress()
            assert int(order_number) in [int(num) for num in order_numbers_in_progress]