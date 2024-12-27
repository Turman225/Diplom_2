from models.api_client import APIClient
import src.data as data


class CreateUserAPI(APIClient):

    def create_user(self, payloads):
        self.post_method(data.CREATE_USER, data=payloads)

    def get_auth_token(self):
        response_body = self.get_response_body
        if 'accessToken' in response_body:
            return response_body['accessToken']
        else:
            return None

    def check_create_user_successfully(self):
        assert self.get_response_body['success'] == True

    def check_create_user_failed(self):
        assert self.get_response_body['success'] == False

    def check_registration_error(self):
        assert self.get_error_msg == "Email, password and name are required fields", \
            f'Фактический результат {self.get_error_msg}'

    def check_user_already_exist_error(self):
        assert self.get_error_msg == "User already exists", \
            f'Фактический результат {self.get_error_msg}'

