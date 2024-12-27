from models.create_order_model import CreateOrderAPI
from models.create_user_model import CreateUserAPI
from models.login_user_model import LoginUserAPI
from models.user_model import UserAPI
from models.get_order_model import GetOrderAPI
from models.delete_user_model import DeleteUserAPI
import src.data as data
import pytest
import requests


@pytest.fixture(scope='function')
def create_user_model():
    response = requests
    create_user_model = CreateUserAPI(response)
    yield create_user_model
    delete_user_model = DeleteUserAPI(response)
    if create_user_model.get_auth_token():
        delete_user_model.delete_user({'Authrization': create_user_model.get_auth_token()})

@pytest.fixture()
def login_user_model():
    response = requests
    login_user_model = LoginUserAPI(response)
    return login_user_model

@pytest.fixture()
def user_model():
    response = requests
    user_model = UserAPI(response)
    return user_model

@pytest.fixture()
def create_order_model():
    response = requests
    create_order_model = CreateOrderAPI(response)
    return create_order_model

@pytest.fixture()
def get_order_model():
    response = requests
    get_order_model = GetOrderAPI(response)
    return get_order_model
