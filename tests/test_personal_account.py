import allure

from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.main_page import login_url
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    @allure.step
    def test_click_personal_account_redirects_to_account(self, driver, main_page, login_page, user):
        """Проверка перехода по клику на «Личный кабинет»"""
        # Логинимся
        login_page.open_login_page()
        login_page.login(user['email'], user['password'])
        # Переходим в личный кабинет
        main_page.click_personal_account()
        # Проверяем, что перешли на страницу аккаунта
        assert "/account" in main_page.current_url() and main_page.find_element(
            PersonalAccountPageLocators.PROFILE_HEADER).is_displayed()

    @allure.step
    def test_click_order_history_navigates_to_history(self, driver, main_page, login_page, user):
        """Проверка перехода в раздел «История заказов»"""
        # Логинимся
        login_page.open_login_page()
        login_page.login(user['email'], user['password'])
        # Переходим в личный кабинет
        main_page.click_personal_account()
        # Переходим в историю заказов
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_order_history()
        # Проверяем, что URL содержит страницу истории заказов
        assert "/order-history" in main_page.current_url()

    @allure.step
    def test_logout_from_account(self, driver, main_page, login_page, user):
        """Проверка выхода из аккаунта"""
        # Логинимся
        login_page.open_login_page()
        login_page.login(user['email'], user['password'])
        # Переходим в личный кабинет
        main_page.click_personal_account()
        # Выходим из аккаунта
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_logout()
        personal_account_page.going_to_login_page()
        assert login_url() == main_page.current_url()
