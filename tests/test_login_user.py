import pytest
import allure
import src.data as data


class TestLoginUser:

    @allure.title("Проверка входа зарегистрированного пользователя с корректными данными")
    def test_login_user(self, login_user_model):
        payloads = data.auth_payload.copy()
        login_user_model.login_user(payloads)
        login_user_model.check_status_code(200)

    @pytest.mark.parametrize('key', ['email', 'password'])
    @allure.title("Проверка входа зарегистрированного пользователя с неверным логином и паролем")
    def test_login_user_validation_error(self, login_user_model, key):
        payloads = data.auth_payload.copy()
        payloads[key] = 'Не верные данные'
        login_user_model.login_user(payloads)
        login_user_model.check_status_code(401)
        login_user_model.check_login_error()
