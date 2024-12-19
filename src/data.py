import src.helper as helper

URL = 'https://stellarburgers.nomoreparties.site'

CREATE_USER = '/api/auth/register'
LOGIN_USER = '/api/auth/login'
USER = '/api/auth/user'
ORDER = '/api/orders'

create_user_payload = {
    "email": f'{helper.create_random_string(8)}@mail.ru',
    "password": helper.create_random_string(12),
    "name": helper.create_random_string(12)
}

generate_params = helper.register_new_user_and_return_params()

created_user_payload = {
    "email": generate_params[0],
    "password": generate_params[1],
    "name": generate_params[2]
}

auth_payload = {
    "email": generate_params[0],
    "password": generate_params[1]
}

patch_user_header = {
    'Authorization': generate_params[3]
}
patch_payload = {"email": generate_params[0].lower(),
                "name": "Меняю Имя"}

ingredients = {
    'Бессмертный краторный бургер': ['61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa6c'],
    'Люминесцентный space краторный бургер': ["61c0c5a71d1f82001bdaaa73", "61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa6c"],
    'invalid hash': ["61c0c5a71d1f8200@DS1bdaaa79","61c0c5a71d1f82001bdaaa6c"]
}

my_account_token = {
    "accessToken": helper.get_my_account_token()[0],
    "refreshToken": helper.get_my_account_token()[1]
}