import pytest
from faker import Faker

fake = Faker()


class TestResults:
    def test_create_result(self, qase, create_project):
        """
        Steps:
        1. Create new run
        2. Create result
        2. Check response
        """
        # cases
        body_cases = {"title": "test case"}
        res_cases = qase.cases.create(code=create_project, body=body_cases)
        assert res_cases.status_code == 200
        assert res_cases.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res_cases.body.get("result").get("id")
        # run
        body = {"title": "test run"}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200
        uuid_run = res.body.get("result").get("id")
        assert uuid_run == 1, "Must be first case"
        # result
        body_result = {"status": "passed", "case_id": uuid_case}
        res = qase.results.create(code=create_project, uuid=uuid_run, body=body_result)
        assert res.status_code == 200

    def test_get_all_results(self, qase, create_project):
        """
        Steps:
        1. Create new case
        2. Create run
        3. Create result
        4. Get all results
        5. Check response
        """
        # cases
        body_cases = {"title": "test case"}
        res_cases = qase.cases.create(code=create_project, body=body_cases)
        assert res_cases.status_code == 200
        assert res_cases.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res_cases.body.get("result").get("id")
        # run
        body = {"title": "test run"}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200
        uuid_run = res.body.get("result").get("id")
        assert uuid_run == 1, "Must be first case"
        # result
        body_result = {"status": "passed", "case_id": uuid_case}
        res = qase.results.create(code=create_project, uuid=uuid_run, body=body_result)
        assert res.status_code == 200
        hash_ = res.body.get("result").get("hash")

        res_results = qase.results.get_all(code=create_project)
        assert res_results.status_code == 200
        results: list = res_results.body.get("result").get("entities")
        is_find = any(project.get("hash") == hash_ for project in results)
        assert is_find, f"Check results in project {create_project}"

    def test_get_result(self, qase, create_project):
        """
        Steps:
        1. Create new run
        2. Create case
        3. Get result by code
        4. Check response
        """
        # cases
        body_cases = {"title": "test case"}
        res_cases = qase.cases.create(code=create_project, body=body_cases)
        assert res_cases.status_code == 200
        assert res_cases.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res_cases.body.get("result").get("id")
        # run
        body = {"title": "test run"}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200
        uuid_run = res.body.get("result").get("id")
        assert uuid_run == 1, "Must be first case"
        # result
        body_result = {"status": "passed", "case_id": uuid_case}
        res = qase.results.create(code=create_project, uuid=uuid_run, body=body_result)
        assert res.status_code == 200
        hash_ = res.body.get("result").get("hash")

        res_result = qase.results.get_result(code=create_project, hash_result=hash_)
        assert res_result.status_code == 200
        assert res_result.body.get("result").get("hash") == hash_

    def test_delete_result(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Create run
        3. Create case
        4. Create result
        5. Delete result
        6. Check response
        """
        # cases
        body_cases = {"title": "test case"}
        res_cases = qase.cases.create(code=create_project, body=body_cases)
        assert res_cases.status_code == 200
        assert res_cases.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res_cases.body.get("result").get("id")
        # run
        body = {"title": "test run"}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200
        uuid_run = res.body.get("result").get("id")
        assert uuid_run == 1, "Must be first case"
        # result
        body_result = {"status": "passed", "case_id": uuid_case}
        res = qase.results.create(code=create_project, uuid=uuid_run, body=body_result)
        assert res.status_code == 200
        hash_ = res.body.get("result").get("hash")

        res_delete = qase.results.delete(
            code=create_project, uuid=uuid_run, hash_result=hash_
        )
        assert res_delete.status_code == 200

    def test_update_result(self, qase, create_project):
        """
        Steps:
        1. Create new run
        2. Create case
        3. Create run
        4. Create result
        5. Update result
        6. Check response
        """
        # cases
        body_cases = {"title": "test case"}
        res_cases = qase.cases.create(code=create_project, body=body_cases)
        assert res_cases.status_code == 200
        assert res_cases.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res_cases.body.get("result").get("id")
        # run
        body = {"title": "test run"}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200
        uuid_run = res.body.get("result").get("id")
        assert uuid_run == 1, "Must be first case"
        # result
        body_result = {"status": "passed", "case_id": uuid_case}
        res = qase.results.create(code=create_project, uuid=uuid_run, body=body_result)
        assert res.status_code == 200
        hash_ = res.body.get("result").get("hash")

        new_body = {"status": "failed"}
        res_update = qase.results.update(
            code=create_project, uuid=uuid_run, hash_result=hash_, body=new_body
        )
        assert res_update.status_code == 200

    @pytest.mark.skip(reason="need to activate bulk in settings")
    def test_bulk(self, qase, create_project):
        """
        Steps:
        1. Create new run
        2. Complete run
        3. Check response
        """
        # cases
        body_cases = {"title": "test case"}
        res_cases = qase.cases.create(code=create_project, body=body_cases)
        assert res_cases.status_code == 200
        assert res_cases.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res_cases.body.get("result").get("id")
        res_cases_2 = qase.cases.create(code=create_project, body=body_cases)
        assert res_cases_2.status_code == 200
        assert res_cases_2.body.get("result").get("id") == 2, "Must be first case"
        uuid_case_2 = res_cases_2.body.get("result").get("id")
        # run
        body = {"title": "test run"}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200
        uuid_run = res.body.get("result").get("id")
        assert uuid_run == 1, "Must be first case"
        # result
        body_result = {"status": "passed", "case_id": uuid_case}
        res = qase.results.create(code=create_project, uuid=uuid_run, body=body_result)
        assert res.status_code == 200

        body_bulk = {
            "results": [
                {"case_id": uuid_case, "status": "passed"},
                {"case_id": uuid_case_2, "status": "failed"},
            ]
        }
        res_bulk = qase.results.bulk(code=create_project, uuid=uuid_run, body=body_bulk)
        assert res_bulk.status_code == 200
