from faker import Faker

fake = Faker()


class TestSharedSteps:
    def test_create_shared_steps(self, qase, create_project):
        """
        Steps:
        1. Create new shared steps
        2. Check response
        """
        body = {"steps": [{"action": "test action"}], "title": "test shared steps"}
        res = qase.shared_steps.create(code=create_project, body=body)
        assert res.status_code == 200
        hash_ = res.body.get("result").get("hash")

        res_delete = qase.shared_steps.delete(
            code=create_project, hash_shared_step=hash_
        )
        assert res_delete.status_code == 200

    def test_get_all_shared_steps(self, qase, create_project):
        """
        Steps:
        1. Create new shared steps
        2. Get all shared steps
        3. Check response
        """
        body = {"steps": [{"action": "test action"}], "title": "test shared steps"}
        res = qase.shared_steps.create(code=create_project, body=body)
        assert res.status_code == 200
        hash_ = res.body.get("result").get("hash")

        res_get_all = qase.shared_steps.get_all(code=create_project)
        assert res_get_all.status_code == 200
        results: list = res_get_all.body.get("result").get("entities")
        is_find = any(step.get("hash") == hash_ for step in results)
        assert is_find, f"Steps with hash {hash_} not found"

        res_delete = qase.shared_steps.delete(
            code=create_project, hash_shared_step=hash_
        )
        assert res_delete.status_code == 200

    def test_get_specific_shared_steps(self, qase, create_project):
        """
        Steps:
        1. Create new shared steps
        2. Get specific shared steps
        3. Check response
        """
        body = {"steps": [{"action": "test action"}], "title": "test shared steps"}
        res = qase.shared_steps.create(code=create_project, body=body)
        assert res.status_code == 200
        hash_ = res.body.get("result").get("hash")

        res_get_step = qase.shared_steps.get_specific_shared_step(
            code=create_project, hash_shared_step=hash_
        )
        assert res_get_step.status_code == 200
        assert res.body.get("result").get("hash") == hash_

        res_delete = qase.shared_steps.delete(
            code=create_project, hash_shared_step=hash_
        )
        assert res_delete.status_code == 200

    def test_update_shared_steps(self, qase, create_project):
        """
        Steps:
        1. Create new shared steps
        2. Update shared step
        3. Check response
        """
        body = {"steps": [{"action": "test action"}], "title": "test shared steps"}
        res = qase.shared_steps.create(code=create_project, body=body)
        assert res.status_code == 200
        hash_ = res.body.get("result").get("hash")

        body_update = {
            "steps": [{"action": "test action"}],
            "title": "test shared steps",
        }
        res_update = qase.shared_steps.update(
            code=create_project, hash_shared_step=hash_, body=body_update
        )
        assert res_update.status_code == 200

        res_delete = qase.shared_steps.delete(
            code=create_project, hash_shared_step=hash_
        )
        assert res_delete.status_code == 200
