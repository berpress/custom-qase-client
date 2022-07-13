from faker import Faker

fake = Faker()


class TestRuns:
    def test_create_run(self, qase, create_project):
        """
        Steps:
        1. Create new run
        2. Check response
        """
        body = {"title": "test run"}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200
        assert res.body.get("result").get("id") == 1, "Must be first case"

    def test_create_run_e2e(self, qase, create_project):
        """
        Steps:
        1. Create case
        2. Create new run
        3. Check response
        """
        # cases
        body_cases = {"title": "test case"}
        res_cases = qase.cases.create(code=create_project, body=body_cases)
        assert res_cases.status_code == 200
        assert res_cases.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res_cases.body.get("result").get("id")
        # runs
        body = {"title": "test run", "cases": [uuid_case]}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200
        assert res.body.get("result").get("id") == 1, "Must be first case"

    def test_get_all_runs(self, qase, create_project):
        """
        Steps:
        1. Create new run
        2. Get all runs
        3. Check response
        """
        name_test_run = "test run"
        body = {"title": name_test_run}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200

        res_runs = qase.runs.get_all(code=create_project)
        assert res_runs.status_code == 200
        results: list = res_runs.body.get("result").get("entities")
        is_find_code = any(project.get("title") == name_test_run for project in results)
        assert is_find_code, f"Check run in project {create_project}"

    def test_get_run_by_id(self, qase, create_project):
        """
        Steps:
        1. Create new run
        2. Get run by id
        3. Check response
        """
        name_test_run = "test run"
        body = {"title": name_test_run}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200
        uuid_run = res.body.get("result").get("id")

        res_run = qase.runs.get_run(code=create_project, uuid=uuid_run)
        assert res_run.status_code == 200
        assert (
            res_run.body.get("result").get("title") == name_test_run
        ), f"Check case in project {create_project}"

    def test_delete_run(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Create run
        3. Delete case
        4. Check response
        """
        body = {"title": "test run"}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200
        assert res.body.get("result").get("id") == 1, "Must be first run"
        uuid_run = res.body.get("result").get("id")

        res_delete = qase.runs.delete(code=create_project, uuid=uuid_run)
        assert res_delete.status_code == 200

    def test_update_run(self, qase, create_project):
        """
        Steps:
        1. Create new run
        2. Update run
        3. Check response
        """
        body = {"title": "test run"}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200
        assert res.body.get("result").get("id") == 1, "Must be first run"
        uuid_run = res.body.get("result").get("id")

        new_body = {"status": True}
        res_update = qase.runs.update(code=create_project, uuid=uuid_run, body=new_body)
        assert res_update.status_code == 200

    def test_complete_run(self, qase, create_project):
        """
        Steps:
        1. Create new run
        2. Complete run
        3. Check response
        """
        body = {"title": "test run"}
        res = qase.runs.create(code=create_project, body=body)
        assert res.status_code == 200
        assert res.body.get("result").get("id") == 1, "Must be first run"
        uuid_run = res.body.get("result").get("id")

        res_complete = qase.runs.complete(code=create_project, uuid=uuid_run)
        assert res_complete.status_code == 200
