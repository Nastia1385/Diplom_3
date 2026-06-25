# helpers.py
import requests
import random
import string
import urls


class UserHelper:
    @staticmethod
    def generate_random_email():
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@test.com"

    @staticmethod
    def generate_random_password():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    @staticmethod
    def generate_random_name():
        return ''.join(random.choices(string.ascii_letters, k=8))

    @staticmethod
    def create_user(email=None, password=None, name=None):
        if not email:
            email = UserHelper.generate_random_email()
        if not password:
            password = UserHelper.generate_random_password()
        if not name:
            name = UserHelper.generate_random_name()

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(f"{urls.API_URL}/auth/register", json=payload)

        if response.status_code == 200:
            data = response.json()
            return {
                "email": email,
                "password": password,
                "name": name,
                "access_token": data.get("accessToken"),
                "refresh_token": data.get("refreshToken"),
                "user_data": data.get("user")
            }
        return None

    @staticmethod
    def delete_user(access_token):
        if access_token:
            headers = {"Authorization": access_token}
            response = requests.delete(f"{urls.API_URL}/auth/user", headers=headers)
            return response.status_code == 200
        return False

    # @staticmethod
    # def login_user(email, password):
    #     payload = {"email": email, "password": password}
    #     response = requests.post(f"{urls.API_URL}/auth/login", json=payload)
    #     if response.status_code == 200:
    #         data = response.json()
    #         return data.get("accessToken")
    #     return None
    #
    # @staticmethod
    # def get_user_orders(access_token):
    #     headers = {"Authorization": access_token}
    #     response = requests.get(f"{urls.API_URL}/orders", headers=headers)
    #     if response.status_code == 200:
    #         data = response.json()
    #         return data.get("orders", [])
    #     return []