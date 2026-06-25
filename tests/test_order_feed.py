import allure
import pytest

from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.step
    def test_click_order_in_feed_opens_details(self, driver, order_feed_page):
        """Проверка открытия всплывающего окна с деталями при клике на заказ в ленте"""
        order_feed_page.open_order_feed_page()
        # Получаем номера заказов
        order_feed_page = OrderFeedPage(driver)
        order_numbers = order_feed_page.get_order_numbers()
        # Кликаем по первому заказу
        order_feed_page.click_order_by_number(order_numbers[0])
        # Проверяем, что открылось модальное окно
        assert order_feed_page.is_order_details_visible()

    @allure.step
    def test_user_orders_visible_in_order_feed(self, driver, main_page, login_page, user):
        """Проверка отображения заказов пользователя на странице Лента заказов"""
        # Логинимся
        login_page.open_login_page()
        login_page.login(user['email'], user['password'])
        # Создаем заказ
        main_page.add_ingredient_to_order()
        main_page.add_bun_to_order()
        main_page.click_order_button()
        order_number = int(main_page.wait_for_order_number_not_9999())
        main_page.close_order_modal()
        # Переходим в ленту заказов
        main_page.click_order_feed()
        # Получаем номера заказов в ленте
        order_feed_page = OrderFeedPage(driver)
        feed_order_numbers = order_feed_page.get_order_numbers()
        # Проверяем, что созданный заказ есть в ленте
        assert order_number in [int(num) for num in feed_order_numbers]

    @pytest.mark.parametrize("counter_method, counter_name", [
        ("get_completed_orders_total", "за всё время"),
        ("get_completed_orders_today", "за сегодня")
    ])
    @allure.step
    def test_create_order_increases_completed_counters(self, driver, main_page, login_page, user, counter_method,
                                                       counter_name):
        """Проверка увеличения счетчиков Выполнено за всё время и Выполнено за сегодня при создании заказа"""
        # Логинимся
        login_page.open_login_page()
        login_page.login(user['email'], user['password'])
        # Переходим в ленту заказов и получаем начальное количество
        main_page.click_order_feed()
        order_feed_page = OrderFeedPage(driver)
        # Получаем начальное значение с помощью метода
        get_counter = getattr(order_feed_page, counter_method)
        initial_value = get_counter()
        # Возвращаемся на главную и создаем заказ
        main_page.click_constructor()
        main_page.add_ingredient_to_order()
        main_page.add_bun_to_order()
        main_page.click_order_button()
        order_number = main_page.wait_for_order_number_not_9999()
        main_page.close_order_modal()
        # Переходим в ленту заказов и получаем новое количество
        main_page.click_order_feed()
        # Получаем новое значение с помощью метода
        new_value = get_counter()
        # Проверяем, что количество увеличилось
        assert new_value > initial_value, f"Счетчик 'Выполнено {counter_name}' не увеличился после создания заказа"

    @allure.step
    def test_order_number_appears_in_progress_after_creation(self, driver, main_page, login_page, user):
        """Проверка появления номера заказа в разделе В работе после оформления"""
        # Логинимся
        login_page.open_login_page()
        login_page.login(user['email'], user['password'])
        # Создаем заказ
        main_page.add_ingredient_to_order()
        main_page.add_bun_to_order()
        main_page.click_order_button()
        order_number = main_page.wait_for_order_number_not_9999()
        main_page.close_order_modal()
        # Переходим в ленту заказов
        main_page.click_order_feed()
        order_feed_page = OrderFeedPage(driver)
        # Получаем заказы в работе
        order_numbers_in_progress = order_feed_page.get_orders_in_progress()
        # Проверяем, что созданный заказ есть в списке
        assert int(order_number) in [int(num) for num in order_numbers_in_progress]
