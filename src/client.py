from src.api.attachments.api import AttachmentsApi
from src.api.cases.api import CasesApi
from src.api.projects.api import ProjectsApi
from src.request import Client


class QaseClient:
    def __init__(self, api_token: str, base_path: str):
        self.client = Client(headers={"Token": api_token})
        self.base_path = base_path

        self.projects = ProjectsApi(self)
        self.cases = CasesApi(self)
        self.attachments = AttachmentsApi(self)
