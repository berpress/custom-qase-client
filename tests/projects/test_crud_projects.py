from faker import Faker

fake = Faker()


class TestAllProjects:
    def test_get_all_projects(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Get all projects
        3. Check project from step 1
        """
        res = qase.projects.get_all_projects()
        assert res.status_code == 200
        results: list = res.body.get("result").get("entities")
        is_find_code = any(
            project.get("code") == create_project.upper() for project in results
        )
        assert is_find_code, f"Check project with code {create_project} in projects"

    def test_get_project_by_code(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Get project by code
        3. Check project from step 1
        """
        res = qase.projects.get_project_by_code(code=create_project.upper())
        assert res.status_code == 200
        assert (
            res.body.get("result").get("code") == create_project.upper()
        ), f"Check project {create_project.upper()}"

    def test_delete_project(self, qase):
        """
        Steps:
        1. Create new project
        2. Delete project from step 1
        3. Check response
        """
        code = fake.first_name()
        body = {"title": f"{code}_title", "code": code, "access": "all"}
        res = qase.projects.create_project(body=body)
        assert res.status_code == 200
        res_delete = qase.projects.delete_project(code=code.upper())
        assert res_delete.status_code == 200
