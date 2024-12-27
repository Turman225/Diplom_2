from models.api_client import APIClient
import src.data as data


class DeleteUserAPI(APIClient):

    def delete_user(self, header):
        self.delete_method(data.USER, headers=header)
