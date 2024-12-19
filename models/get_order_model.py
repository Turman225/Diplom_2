from models.api_client import APIClient
import src.data as data


class GetOrderAPI(APIClient):

    def get_orders(self, token):
        self.get_method(data.ORDER, headers=token)

    def check_order_list_not_empty(self):
        assert len(self.get_response_body['orders']) != 0

    def check_error_get_order_with_unauthorized_user(self):
        assert self.get_error_msg == 'You should be authorised'