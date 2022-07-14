import pytest

from faker import Faker

from cqase.client import QaseClient

fake = Faker()


def pytest_addoption(parser):
    parser.addoption(
        "--api-token",
        action="store",
        help="enter qase api token",
    ),


@pytest.fixture(scope="session")
def qase(request):
    api_token = request.config.getoption("--core-url")
    url = "https://api.qase.io/v1"
    client = QaseClient(api_token=api_token, base_path=url)
    yield client


@pytest.fixture()
def create_project(qase):
    code = fake.first_name()
    body = {"title": f"{code} test project", "code": code, "access": "all"}
    res = qase.projects.create(body=body)
    assert res.status_code == 200
    yield code.upper()
    res_delete = qase.projects.delete(code=code.upper())
    assert res_delete.status_code == 200
