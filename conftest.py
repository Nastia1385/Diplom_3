import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_account_page import PersonalAccountPage
from pages.order_feed_page import OrderFeedPage
from helpers import UserHelper

@pytest.fixture(params=['Chrome'], scope="function")
def driver(request):
    """Параметризованная фикстура для запуска в разных браузерах"""
    browser_name = request.param

    if browser_name == 'Chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    else:  # Firefox
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def password_recovery_page(driver):
    return PasswordRecoveryPage(driver)


@pytest.fixture
def personal_account_page(driver):
    return PersonalAccountPage(driver)


@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture
def user():
    """Создание тестового пользователя через API"""
    user_data = UserHelper.create_user()
    yield user_data
    # Удаление пользователя после теста
    if user_data and user_data.get('access_token'):
        UserHelper.delete_user(user_data.get('access_token'))


@pytest.fixture
def user_without_delete():
    """Создание тестового пользователя без автоматического удаления (для тестов, где удаление вручную)"""
    user_data = UserHelper.create_user()
    yield user_data