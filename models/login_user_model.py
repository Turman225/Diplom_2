from models.api_client import APIClient
import src.data as data


class LoginUserAPI(APIClient):

    def login_user(self, payload):
        self.post_method(data.LOGIN_USER, data=payload)

    def check_login_error(self):
        assert self.get_error_msg == "email or password are incorrect"