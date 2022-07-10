from src.api.cases.api import CasesApi
from src.api.projects.api import ProjectsApi
from src.request import Client


class QaseClient:
    def __init__(self, api_token: str, base_path: str):
        self.client = Client()
        self.api_token = api_token
        self.base_path = base_path
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Token": self.api_token,
        }

        self.projects = ProjectsApi(self)
        self.cases = CasesApi(self)
