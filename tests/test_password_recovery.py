import allure

import urls


class TestPasswordRecovery:

    @allure.step
    def test_click_password_recovery_link_redirects_to_recovery_page(self, driver, login_page, password_recovery_page):
        """Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»"""
        login_page.open_login_page()
        login_page.click_password_recovery()
        # Проверяем, что мы на странице восстановления пароля
        assert driver.current_url == urls.PASSWORD_RECOVERY_URL

    @allure.step
    def test_enter_email_and_click_recover(self, driver, password_recovery_page, user):
        """Проверка ввода почты и клика по кнопке «Восстановить»"""
        password_recovery_page.open_password_recovery_page()
        # Вводим email существующего пользователя
        password_recovery_page.enter_email_for_recovery(user['email'])
        password_recovery_page.click_recover_button()
        # Ожидаем перехода на страницу сброса пароля
        # WebDriverWait(driver, 10).until(
        #     EC.url_contains("/forgot-password")
        # )
        # Проверяем, что произошел переход на страницу сброса пароля
        assert "forgot-password" in driver.current_url

    @allure.step
    def test_show_password_button_highlights_field(self, driver, password_recovery_page, user):
        """Проверка клика по кнопке показать/скрыть пароль - поле становится активным"""
        password_recovery_page.open_password_recovery_page()
        # Вводим почту существующего пользователя
        password_recovery_page.enter_email_for_recovery(user['email'])
        password_recovery_page.click_recover_button()

        # Ожидаем перехода на страницу сброса пароля
        # password_recovery_page.wait_for_reset_password_page()

        # # Ожидаем появления поля для ввода нового пароля
        # password_recovery_page.wait_for_password_field()

        # Получаем класс до клика
        class_before = password_recovery_page.get_password_input_class()

        # Проверяем, что класс не содержит active до клика
        # assert "input_status_active" not in class_before

        # Получаем тип поля до клика (должен быть password)
        type_before = password_recovery_page.get_password_input_type()
        # assert type_before == "password"

        # Кликаем по кнопке показать пароль
        password_recovery_page.show_password()

        # Получаем класс после клика
        class_after = password_recovery_page.get_password_input_class()

        # Проверяем, что класс изменился - добавился input_status_active
        assert "input_status_active" in class_after and class_before != class_after


