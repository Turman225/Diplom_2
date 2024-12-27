import pytest
import allure
import src.data as data


class TestUser:


    @allure.title("Проверка изменения данных авторизованного пользователя пользователя")
    def test_edit_user_data(self, user_model):
        user_model.patch_user(data.patch_user_header, data.patch_payload)
        user_model.check_status_code(200)
        user_model.check_user_data_change(data.patch_payload)

    @allure.title("Проверка изменения данных не авторизованного пользователя пользователя")
    @pytest.mark.parametrize('key, value', [('name', 'Меняю имя'), ('email', data.create_user_payload['email'])])
    def test_edit_user_data_without_authorization(self, user_model, key, value):
        user_model.patch_user(None, {key: value})
        user_model.check_status_code(401)
        user_model.check_error_change_data_without_authorization()