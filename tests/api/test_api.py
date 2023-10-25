import allure
import pytest
from framework.api_methods.main_page import ApiMethodsPages


@pytest.mark.positive
@allure.epic('Проверка API Swagger\'a')
@allure.feature('Test Swagger API')
class TestSwaggerApi:

    @allure.epic('Проверка API Swagger\'a')
    @allure.feature('Test Swagger API')
    @allure.story('Отправка POST запроса')
    def test_order_post(self, request_session):

        body = {
            "id": 1,
            "petId": 0,
            "quantity": 0,
            "shipDate": "2023-10-17T17:41:50.782Z",
            "status": "placed",
            "complete": True
        }

        session = ApiMethodsPages()
        with allure.step('Отправка POST запроса'):
            response = session.send_post(request_session, body)

        with allure.step('Проверка JSON схемы'):
            assert session.check_json_scheme(response, body) == True

        with allure.step('Проверка что id питомца в ответе не равно нулю'):
            assert session.id_not_zero(response) == True

    @allure.epic('Проверка API Swagger\'a')
    @allure.feature('Test Swagger API')
    @allure.story('Отправка GET запроса OrderId')
    @pytest.mark.usefixtures('preload_requests')
    def test_order_id_get(self, request_session):
        session = ApiMethodsPages()

        with allure.step('Отправка GET запроса'):
            response = session.send_get(request_session, 3)

        with allure.step('Проверка что в ответе пришел JSON'):
            assert session.check_response_on_json(response) == True

    @allure.epic('Проверка API Swagger\'a')
    @allure.feature('Test Swagger API')
    @allure.story('Отправка DELETE запроса OrderId')
    @pytest.mark.usefixtures('preload_requests')
    def test_order_delete(self, request_session):
        session = ApiMethodsPages()
        order_id = 3

        with allure.step('Отправка DELETE запроса'):
            response = session.send_delete(request_session, order_id)

        with allure.step('Проверка на соответствие удаленного orderId с Id указанным в ответе'):
            assert session.check_response_text_on_pet_id(response, order_id) == True

        with allure.step('Проверка Id после удаления'):
            assert session.check_id_after_remove(request_session, order_id) == True

    @allure.epic('Проверка API Swagger\'a')
    @allure.feature('Test Swagger API')
    @allure.story('Отправка GET запроса к Inventory')
    def test_inventory_get(self, request_session):
        session = ApiMethodsPages()

        with allure.step('Отправка GET запроса к Inventory'):
            response = session.send_get_inventory(request_session)
        