import pytest
import requests
import allure

class TestListOrders:
    @allure.title("Получение списка всех заказов")
    def test_get_list_orders(self):
        response = requests.get('http://qa-scooter.praktikum-services.ru/api/v1/orders')
        assert response.status_code == 200 and 'orders' in response.text


