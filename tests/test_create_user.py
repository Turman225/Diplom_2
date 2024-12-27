import pytest
import allure
import src.data as data


class TestCreateUser:

    @allure.title("Проверка создания пользователя с корректными данными")
    def test_create_user(self, create_user_model):
        create_user_model.create_user(data.create_user_payload)
        create_user_model.check_status_code(200)
        print(create_user_model.get_auth_token())
        create_user_model.check_create_user_successfully()

    @allure.title("Проверка вывода ошибки при создании пользователя без почты, логина или пароля")
    @pytest.mark.parametrize('key', ["email", "password", "name"])
    def test_create_user_validation_error_on_empty_required_fields(self, create_user_model, key):
        payload = data.create_user_payload.copy()
        payload[key] = None
        create_user_model.create_user(payload)
        print(create_user_model.get_auth_token())
        create_user_model.check_status_code(403)
        create_user_model.check_registration_error()

    @allure.title("Проверка вывода ошибки при создании пользователя с данными которые уже зарегистрированы")
    def test_error_on_duplicate_user_creation(self, create_user_model):
        create_user_model.create_user(data.created_user_payload)
        create_user_model.check_status_code(403)
        print(create_user_model.get_auth_token())
        create_user_model.check_create_user_failed()
        create_user_model.check_user_already_exist_error()