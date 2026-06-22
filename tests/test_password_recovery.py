# tests/test_password_recovery.py
import pytest
from pages.password_recovery_page import PasswordRecoveryPage
from pages.login_page import LoginPage
import urls


class TestPasswordRecovery:

    def test_click_password_recovery_link_redirects_to_recovery_page(self, driver, login_page, password_recovery_page):
        """Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»"""
        login_page.open_login_page()
        login_page.click_password_recovery()

        # Проверяем, что мы на странице восстановления пароля
        assert driver.current_url == urls.PASSWORD_RECOVERY_URL

    def test_enter_email_and_click_recover(self, password_recovery_page):
        """Проверка ввода почты и клика по кнопке «Восстановить»"""
        password_recovery_page.open_password_recovery_page()
        password_recovery_page.enter_email_for_recovery("test@test.com")
        password_recovery_page.click_recover_button()

        # Проверяем, что произошел переход на страницу сброса пароля
        # URL должен содержать reset-password
        assert "reset-password" in password_recovery_page.driver.current_url

    def test_show_password_button_highlights_field(self, password_recovery_page):
        """Проверка клика по кнопке показать/скрыть пароль - поле становится активным"""
        password_recovery_page.open_password_recovery_page()

        # Вводим почту и нажимаем восстановить для перехода к форме сброса
        password_recovery_page.enter_email_for_recovery("test@test.com")
        password_recovery_page.click_recover_button()

        # Получаем класс до клика
        initial_class = password_recovery_page.get_password_input_container_class()

        # Кликаем по кнопке показать пароль
        password_recovery_page.show_password()

        # Получаем класс после клика
        new_class = password_recovery_page.get_password_input_container_class()

        # Проверяем, что класс изменился (стал активным)
        # Обычно при активации добавляется класс 'input_status_active'
        assert initial_class != new_class or 'active' in new_class.lower()