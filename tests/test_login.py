import requests
from tests.helpers import register_new_courier_and_return_login_password
from tests.helpers import generating_cred
import allure
import json

class TestLogin:

    @allure.title("Авторизация с валидными данными")
    def test_login_success(self):
        login, password, name = register_new_courier_and_return_login_password()
        payload = {
            'login': login,
            'password': password
        }
        response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 200

    @allure.title("Проверка возврата id при авторизации")
    def test_login_get_id(self):
        login, password, name = register_new_courier_and_return_login_password()
        payload = {
            'login': login,
            'password': password
        }
        response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload).json()
        assert 'id' in response

    @allure.title("Ошибка при авторизации без пароля ")
    def test_login_no_password(self):
        login, password, name = register_new_courier_and_return_login_password()
        payload = {
            'login': login
        }
        response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 504
        assert response.text == 'Service unavailable'

    @allure.title("Ошибка при авторизации без логина")
    def test_login_no_login(self):
        login, password, name = register_new_courier_and_return_login_password()
        payload = {
            'password': password
        }
        response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.text == '{"code":400,"message":"Недостаточно данных для входа"}'

    @allure.title("Ошибка при авторизации с неверным паролем")
    def test_login_bad_password(self):
        login, password, name = register_new_courier_and_return_login_password()
        payload = {
            'login': login,
            'password': 12345
        }
        response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload).json()
        assert response['code'] == 404
        assert response['message'] == 'Учетная запись не найдена'

    @allure.title("Ошибка при авторизации с неверным логином")
    def test_login_bad_login(self):
        login, password, name = register_new_courier_and_return_login_password()
        payload = {
            'login': '12345',
            'password': password
        }
        response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload).json()
        assert response['code'] == 404
        assert response['message'] == 'Учетная запись не найдена'

    @allure.title("Ошибка при авторизации с неверными данными")
    def test_login_invalid_data(self):
        payload = {
            'login': generating_cred()['login'],
            'password': generating_cred()['password']
        }
        response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload).json()
        assert response['code'] == 404
        assert response['message'] == 'Учетная запись не найдена'














