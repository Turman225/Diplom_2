import pytest
import allure
import src.data as data


class TestCreateOrder:

    @allure.title("Проверка создания заказа с добавлением ингредиентов пользователем с авторизацией и без")
    @pytest.mark.parametrize('ingregients, header', [('Бессмертный краторный бургер', None),
                                                     ('Люминесцентный space краторный бургер', {'Authorization': data.my_account_token['accessToken']})])
    def test_create_order(self, create_order_model, ingregients, header):
        create_order_model.create_order(header, {'ingredients': data.ingredients[ingregients]})
        create_order_model.check_status_code(200)
        create_order_model.check_order_has_been_created(ingregients)

    @allure.title("Проверка создания заказа без ингредиентов пользователем с авторизацией и без")
    @pytest.mark.parametrize('header', [None, {'Authorization': data.my_account_token['accessToken']}])
    def test_create_order_on_empty_ingredients(self, create_order_model, header):
        create_order_model.create_order(header, {'ingredients': None})
        create_order_model.check_status_code(400)
        create_order_model.check_error_create_order()

    @allure.title("Проверка создания заказа с добавлением неверного хеша ингредиента")
    @pytest.mark.parametrize('header', [None, {'Authorization': data.my_account_token['accessToken']}])
    def test_create_order_on_invalid_hash_ingredients(self, create_order_model, header):
        create_order_model.create_order(header, {'ingredients': data.ingredients['invalid hash']})
        create_order_model.check_status_code(500)
