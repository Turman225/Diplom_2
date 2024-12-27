from models.api_client import APIClient
import src.data as data


class UserAPI(APIClient):

    def patch_user(self, header, payload):
        self.patch_method(data.USER, headers=header, json=payload)

    def check_user_data_change(self, expected_data):
        assert self.get_response_body['user'] == expected_data, (
            f"Фактический результат {self.get_response_body['user']} != {expected_data}")

    def check_error_change_data_without_authorization(self):
        assert self.get_error_msg == 'You should be authorised'