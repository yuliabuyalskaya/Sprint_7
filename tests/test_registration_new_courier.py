import allure
import requests
from tests.helpers import generating_cred

class TestRegistrationNewCourier:

    @allure.title("Правильный статус код ответа при регистарции курьера")
    def test_register_new_courier_success(self):
        payload = generating_cred()
        response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert response.status_code == 201

    @allure.title("Правильное сообщение при регистрации курьера")
    def test_register_new_courier_success_message(self):
        payload = generating_cred()
        response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload).json()
        assert response['ok'] == True

    @allure.title("ТОшибка при повторной регистрации такого же курьера")
    def test_new_courier_registration_existing_courier(self):
        response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data={
    "login": "nikita",
    "password": "12345",
    "firstName": "nikita12345"}).json()
        assert response['code'] == 409
        assert response['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title("Регистрация с существующим логином")
    def test_new_courier_registration_existing_login(self):
        payload = generating_cred()
        payload['login'] = 'nikita'
        response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload).json()
        assert response['code'] == 409
        assert response['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title("Регистрация без логина и пароля")
    def test_new_courier_registration_no_login_and_password(self):
        response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data={
            "firstName": "nikita12345"}).json()
        assert response['code'] == 400
        assert response['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title("Регистрация без имени и пароля")
    def test_new_courier_registration_no_name_and_password(self):
        response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data={
            "login": "nikita123453"}).json()
        assert response['code'] == 400
        assert response['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title("Регистрация без имени и логина")
    def test_new_courier_registration_no_name_and_login(self):
        response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data={
            "password": "nikita1234531"}).json()
        assert response['code'] == 400
        assert response['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title("Регистрация без пароля")
    def test_new_courier_registration_no_password(self):
        payload = generating_cred().pop('password')
        response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title("Регистрация без логина")
    def test_new_courier_registration_no_login(self):
        payload = generating_cred().pop('login')
        response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title("Регистрация без имени")
    def test_new_courier_registration_no_name(self):
        payload = generating_cred().pop('firstName')
        response = requests.post("http://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'






