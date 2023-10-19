import json


class ApiMethodsPages:
    URL = 'https://petstore.swagger.io/v2/store/order/'

    def send_post(self, session, body: dict):
        headers = {
            "content-type": "application/json"
        }
        response = session.post(self.URL, headers=headers, data=json.dumps(body))
        if self.check_response(response):
            return response.json()
        return False

    def send_get(self, session, order_id: int):
        response = session.get(f"{self.URL}{order_id}")
        if self.check_response(response):
            return response.json()
        return False

    def send_delete(self, session, order_id: int):
        response = session.delete(f'{self.URL}{order_id}')
        if self.check_response(response):
            return response.json()
        return False

    def send_get_inventory(self, session):
        response = session.get('https://petstore.swagger.io/v2/store/inventory/')
        if self.check_response(response):
            return response.json()
        return False
    def check_response(self, response):
        if response.status_code != 200:
            return False
        return True
    def check_json_scheme(self, response, body):
        return response.keys() == body.keys()

    def id_not_zero(self, response):
        return response["id"] > 0

    def check_response_on_json(self, response):
        return type(response) == dict

    def check_response_text_on_pet_id(self, response: dict, order_id: int):
        if int(response['message']) == order_id:
            return True
        return False

    def check_id_after_remove(self, session, order_id:int):
        response = session.get(f'{self.URL}{order_id}')
        if response.json()['message'] == "Order not found":
            return True
        return False