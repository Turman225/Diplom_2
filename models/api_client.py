import requests
import allure
import src.data as data


class APIClient():

    def __init__(self, response):
        self.response = response

    @allure.step('Отправляем POST запрос')
    def post_method(self, endpoint, **kwargs):
        self.response = requests.post(f'{data.URL}{endpoint}', **kwargs)
        return self.response

    @allure.step('Отправляем DELETE запрос')
    def delete_method(self, endpoint, **kwargs):
        self.response = requests.delete(f'{data.URL}{endpoint}', **kwargs)
        return self.response

    def patch_method(self, endpoint, **kwargs):
        self.response = requests.patch(f'{data.URL}{endpoint}', **kwargs)
        return self.response

    def get_method(self, endpoint, **kwargs):
        self.response = requests.get(f'{data.URL}{endpoint}', **kwargs)
        return self.response

    @property
    def get_response_body(self):
        return self.response.json()

    @property
    def get_error_msg(self):
        return self.get_response_body['message']

    @allure.step('Проверяем статус код')
    def check_status_code(self, code):
        print(self.response.status_code)
        assert self.response.status_code == code

