import pytest

from faker import Faker

from src.client import QaseClient

fake = Faker()


@pytest.fixture(scope="session")
def qase():
    url = "https://api.qase.io/v1"
    token = "xxxx"
    client = QaseClient(api_token=token, base_path=url)
    yield client


@pytest.fixture()
def create_project(qase):
    code = fake.first_name()
    body = {"title": f"{code}_title", "code": code, "access": "all"}
    res = qase.projects.create_project(body=body)
    assert res.status_code == 200
    yield code.upper()
    res_delete = qase.projects.delete_project(code=code.upper())
    assert res_delete.status_code == 200
