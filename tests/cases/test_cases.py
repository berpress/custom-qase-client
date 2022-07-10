from faker import Faker

fake = Faker()


class TestCases:
    def test_create_case(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Create case
        3. Check response
        """
        body = {"title": "test case"}
        res = qase.cases.create_case(code=create_project, body=body)
        assert res.status_code == 200
        assert res.body.get("result").get("id") == 1, "Must be first case"

    def test_get_all_cases(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Create case
        3. Get all cases
        4. Check response
        """
        name_test_case = "test case"
        body = {"title": name_test_case}
        res = qase.cases.create_case(code=create_project, body=body)
        assert res.status_code == 200

        res_cases = qase.cases.get_all_cases(code=create_project)
        assert res_cases.status_code == 200
        results: list = res_cases.body.get("result").get("entities")
        is_find_code = any(
            project.get("title") == name_test_case for project in results
        )
        assert is_find_code, f"Check case in project {create_project}"

    def test_get_case_by_id(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Create case
        3. Get case by id
        4. Check response
        """
        name_test_case = "test case"
        body = {"title": name_test_case}
        res = qase.cases.create_case(code=create_project, body=body)
        assert res.status_code == 200
        uuid_case = res.body.get("result").get("id")

        res_case = qase.cases.get_case_by_id(code=create_project, uuid=uuid_case)
        assert res_case.status_code == 200
        assert (
            res_case.body.get("result").get("title") == name_test_case
        ), f"Check case in project {create_project}"

    def test_delete_case(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Create case
        3. Delete case
        4. Check response
        """
        body = {"title": "test case"}
        res = qase.cases.create_case(code=create_project, body=body)
        assert res.status_code == 200
        assert res.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res.body.get("result").get("id")

        res_delete = qase.cases.delete_case(code=create_project, uuid=uuid_case)
        assert res_delete.status_code == 200

    def test_update_case(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Create case
        3. Update case
        4. Check response
        """
        body = {"title": "test case"}
        res = qase.cases.create_case(code=create_project, body=body)
        assert res.status_code == 200
        assert res.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res.body.get("result").get("id")

        name_test_case = "new test case"
        body["title"] = name_test_case
        res_update = qase.cases.update_case(
            code=create_project, uuid=uuid_case, body=body
        )
        assert res_update.status_code == 200

        res_case = qase.cases.get_case_by_id(code=create_project, uuid=uuid_case)
        assert res_case.status_code == 200
        assert (
            res_case.body.get("result").get("title") == name_test_case
        ), f"Check case in project {create_project}"
