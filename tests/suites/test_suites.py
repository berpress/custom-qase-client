from faker import Faker

fake = Faker()


class TestSuites:
    def test_create_suites(self, qase, create_project):
        """
        Steps:
        1. Create new suite
        2. Check response
        """
        body = {"title": "test suit"}
        res = qase.suites.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_delete = qase.suites.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_get_all_shared_suites(self, qase, create_project):
        """
        Steps:
        1. Create new suite
        2. Get all suites
        3. Check response
        """
        body = {"title": "test suit"}
        res = qase.suites.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_get_all = qase.suites.get_all(code=create_project)
        assert res_get_all.status_code == 200
        results: list = res_get_all.body.get("result").get("entities")
        is_find = any(suit.get("id") == id_ for suit in results)
        assert is_find, f"Suit with id {id_} not found"

        res_delete = qase.suites.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_get_specific_suite(self, qase, create_project):
        """
        Steps:
        1. Create new suite
        2. Get specific suite
        3. Check response
        """
        body = {"title": "test suit"}
        res = qase.suites.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_get_suit = qase.suites.get_specific_suit(code=create_project, uuid=id_)
        assert res_get_suit.status_code == 200
        assert res.body.get("result").get("id") == id_

        res_delete = qase.suites.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_update_shared_suite(self, qase, create_project):
        """
        Steps:
        1. Create new suite
        2. Update suite
        3. Check response
        """
        body = {"title": "test suit"}
        res = qase.suites.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        body_update = {"title": "test suit new"}
        res_update = qase.suites.update(code=create_project, uuid=id_, body=body_update)
        assert res_update.status_code == 200

        res_delete = qase.suites.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200
