from models.api_client import APIClient
import src.data as data


class CreateOrderAPI(APIClient):

    def create_order(self, header, payload):
        self.post_method(data.ORDER, headers=header, data=payload)

    def check_order_has_been_created(self, burger):
        assert (self.get_response_body['name'] == burger) and (self.get_response_body['success'] == True)

    def check_error_create_order(self):
        assert self.get_error_msg == 'Ingredient ids must be provided'