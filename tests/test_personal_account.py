from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.personal_account_page import PersonalAccountPage
import urls


class TestPersonalAccount:

    def test_click_personal_account_redirects_to_account(self, driver, main_page, login_page, user):
        """Проверка перехода по клику на «Личный кабинет»"""
        # Логинимся
        login_page.open_login_page()
        login_page.login(user['email'], user['password'])
        # Переходим в личный кабинет
        main_page.click_personal_account()
        # Проверяем, что перешли на страницу аккаунта
        assert "/account" in driver.current_url
        assert main_page.find_element(PersonalAccountPageLocators.PROFILE_HEADER).is_displayed()

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
        assert "/order-history" in driver.current_url

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
        # Проверяем, что перешли на страницу логина
        WebDriverWait(driver, 10).until(EC.url_to_be(urls.LOGIN_URL))
        assert driver.current_url == urls.LOGIN_URL