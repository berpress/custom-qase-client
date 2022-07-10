from src.models import ResponseModel


class CasesApi:
    def __init__(self, app):
        self.app = app

    _POST_CREATE_CASE = "/case/{}"
    _GET_ALL_TEST_CASES = "/case/{}"
    _GET_CASE_BY_ID = "/case/{}/{}"
    _DELETE_CASE = "/case/{}/{}"
    _UPDATE_CASE = "/case/{}/{}"

    def create_case(self, code: str, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/create-case
        """
        return self.app.client.request(
            method="POST",
            url=f"{self.app.base_path}{self._POST_CREATE_CASE.format(code)}",
            json=body,
            headers=self.app.headers,
        )

    def get_all_cases(self, code: str, params: dict = None) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-cases
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_ALL_TEST_CASES.format(code)}",
            params=params,
            headers=self.app.headers,
        )

    def get_case_by_id(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/get-case
        """
        return self.app.client.request(
            method="GET",
            url=f"{self.app.base_path}{self._GET_CASE_BY_ID.format(code, uuid)}",
            headers=self.app.headers,
        )

    def delete_case(self, code: str, uuid: int) -> ResponseModel:
        """
        https://developers.qase.io/reference/delete-case
        """
        return self.app.client.request(
            method="DELETE",
            url=f"{self.app.base_path}{self._DELETE_CASE.format(code, uuid)}",
            headers=self.app.headers,
        )

    def update_case(self, code: str, uuid: int, body: dict) -> ResponseModel:
        """
        https://developers.qase.io/reference/update-case
        """
        return self.app.client.request(
            method="PATCH",
            url=f"{self.app.base_path}{self._UPDATE_CASE.format(code, uuid)}",
            json=body,
            headers=self.app.headers,
        )
