from src.api.attachments.api import AttachmentsApi
from src.api.cases.api import CasesApi
from src.api.custom_fields.api import CustomFieldsApi
from src.api.defects.api import DefectsApi
from src.api.environments.api import EnvironmentsApi
from src.api.milestones.api import MilestoneApi
from src.api.projects.api import ProjectsApi
from src.request import Client


class QaseClient:
    def __init__(self, api_token: str, base_path: str):
        self.client = Client(headers={"Token": api_token})
        self.base_path = base_path

        self.projects = ProjectsApi(self)
        self.cases = CasesApi(self)
        self.attachments = AttachmentsApi(self)
        self.custom_fields = CustomFieldsApi(self)
        self.defects = DefectsApi(self)
        self.environments = EnvironmentsApi(self)
        self.milestones = MilestoneApi(self)
