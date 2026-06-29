import allure
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.main_page import login_url
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    @allure.title("Переход в личный кабинет по клику на кнопку")
    def test_click_personal_account_redirects_to_account(self, driver, main_page, login_page, user):
        with allure.step("Открыть страницу логина и авторизоваться"):
            login_page.open_login_page()
            login_page.login(user['email'], user['password'])

        with allure.step("Кликнуть на «Личный кабинет»"):
            main_page.click_personal_account()

        with allure.step("Проверить переход на страницу аккаунта"):
            assert "/account" in main_page.current_url() and main_page.find_element(
                PersonalAccountPageLocators.PROFILE_HEADER).is_displayed()

    @allure.title("Переход в раздел «История заказов»")
    def test_click_order_history_navigates_to_history(self, driver, main_page, login_page, user):
        with allure.step("Открыть страницу логина и авторизоваться"):
            login_page.open_login_page()
            login_page.login(user['email'], user['password'])

        with allure.step("Кликнуть на «Личный кабинет»"):
            main_page.click_personal_account()

        with allure.step("Перейти в историю заказов"):
            personal_account_page = PersonalAccountPage(driver)
            personal_account_page.click_order_history()

        with allure.step("Проверить URL страницы истории заказов"):
            assert "/order-history" in main_page.current_url()

    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, driver, main_page, login_page, user):
        with allure.step("Открыть страницу логина и авторизоваться"):
            login_page.open_login_page()
            login_page.login(user['email'], user['password'])

        with allure.step("Кликнуть на «Личный кабинет»"):
            main_page.click_personal_account()

        with allure.step("Выйти из аккаунта"):
            personal_account_page = PersonalAccountPage(driver)
            personal_account_page.click_logout()
            personal_account_page.going_to_login_page()

        with allure.step("Проверить переход на страницу логина"):
            assert login_url() == main_page.current_url()