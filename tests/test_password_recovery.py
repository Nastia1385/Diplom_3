import allure
import urls


class TestPasswordRecovery:

    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_click_password_recovery_link_redirects_to_recovery_page(self, driver, login_page, password_recovery_page,
                                                                     main_page):
        """Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»"""
        login_page.open_login_page()
        login_page.click_password_recovery()
        # Проверяем, что мы на странице восстановления пароля
        assert urls.PASSWORD_RECOVERY_URL == main_page.current_url()

    @allure.title("Проверка ввода почты и клика по кнопке «Восстановить»")
    def test_enter_email_and_click_recover(self, driver, password_recovery_page, user, main_page):
        """Проверка ввода почты и клика по кнопке «Восстановить»"""
        password_recovery_page.open_password_recovery_page()
        # Вводим email существующего пользователя
        password_recovery_page.enter_email_for_recovery(user['email'])
        password_recovery_page.click_recover_button()
        assert "forgot-password" in main_page.current_url()

    @allure.title("Проверка клика по кнопке показать/скрыть пароль - поле становится активным")
    def test_show_password_button_highlights_field(self, driver, password_recovery_page, user):
        """Проверка клика по кнопке показать/скрыть пароль - поле становится активным"""
        password_recovery_page.open_password_recovery_page()
        # Вводим почту существующего пользователя
        password_recovery_page.enter_email_for_recovery(user['email'])
        password_recovery_page.click_recover_button()
        # Получаем класс до клика
        class_before = password_recovery_page.get_password_input_class()
        # Кликаем по кнопке показать пароль
        password_recovery_page.show_password()
        # Получаем класс после клика
        class_after = password_recovery_page.get_password_input_class()
        # Проверяем, что класс изменился - добавился input_status_active
        assert "input_status_active" in class_after and class_before != class_after