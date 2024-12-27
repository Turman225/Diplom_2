import random
import string
import requests


def create_random_string(lenth):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(lenth))
    return random_string

def register_new_user_and_return_params():

# создаём список, чтобы метод мог его вернуть
    login_pass = []
    # генерируем логин, пароль и имя курьера
    email = f'{create_random_string(8)}@mail.ru'
    password = create_random_string(12)
    name = create_random_string(12)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
    access_token = response.json()['accessToken']
    refresh_token = response.json()['refreshToken']

    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)
        login_pass.append(access_token)
        login_pass.append(refresh_token)
    else:
        print("Регистрация провалена")

    # возвращаем список
    return login_pass

def get_my_account_token():

    my_tokens = []

    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/login', json={
                                                                                        "email": "turman225@mail.ru",
                                                                                        "password": "123123"
                                                                                        })
    access_token = response.json()['accessToken']
    refresh_token = response.json()['refreshToken']

    if response.status_code == 200:
        my_tokens.append(access_token)
        my_tokens.append(refresh_token)
    else:
        print("Вход не выполнен")

    return my_tokens