
import allure
import pytest
import requests

class TestOrdersCourier:
    @pytest.mark.parametrize(
        'firstname, lastname, address, metrostation, phone, rentTime, deliveryDate, comment, color',
        [
            ('Никита', 'Кулешов', 'Товарищевский пр д 31', 'Девиткино', '79654562134', '5', '2020-06-06',
             'Saske, come back to Konoha', ['BLACK']),
            ('Никита', 'Бубрешов', 'Товарищевский пр д 32', 'Девяткино', '79654562133', '4', '2020-06-07',
             'Saske, come back to Konoha', ['GREY']),
            ('Никита', 'Кулешов', 'Товарищевский пр д 31', 'Девиткино', '79654562134', '5', '2020-06-06',
             'Saske, come back to Konoha', ['BLACK', 'GREY']),
            ('Никита', 'Бубрешов', 'Товарищевский пр д 32', 'Девяткино', '79654562133', '4', '2020-06-07',
             'Saske, come back to Konoha', [])
        ]
    )
    @allure.title("Проверка создания заказа с разными цветами")
    def test_order_color_confirm(self, firstname, lastname, address, metrostation, phone, rentTime, deliveryDate,
                                 comment, color):
        payload = {
            "firstName": firstname,
            "lastName": lastname,
            "address": address,
            "metroStation": metrostation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": color
        }

        response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/orders', json=payload)
        assert response.status_code == 201
        assert 'track' in response.text







