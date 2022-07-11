from faker import Faker

fake = Faker()


class TestDefects:
    def test_create_defects(self, qase, create_project):
        """
        Steps:
        1. Create defects
        2. Check response
        """
        body = {
            "title": f"{fake.first_name()} test defect",
            "actual_result": "result",
            "severity": 1,
        }
        res = qase.defects.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_delete = qase.defects.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_get_all_defects(self, qase, create_project):
        """
        Steps:
        1. Create defects
        2. Get all defects
        3. Check response
        """
        defect_title = f"{fake.first_name()} test defect"
        body = {"title": defect_title, "actual_result": "result", "severity": 1}
        res = qase.defects.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_get_all = qase.defects.get_all(code=create_project)
        assert res_get_all.status_code == 200
        results: list = res_get_all.body.get("result").get("entities")
        is_find_field = any(project.get("title") == defect_title for project in results)
        assert is_find_field, f"Defect {defect_title} not found"

        res_delete = qase.defects.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_get_specific_defects(self, qase, create_project):
        """
        Steps:
        1. Create defects
        2. Get specific defect
        3. Check response
        """
        defect_title = f"{fake.first_name()} test defect"
        body = {"title": f"{defect_title}", "actual_result": "result", "severity": 1}
        res = qase.defects.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_get_defect = qase.defects.get_specific_defect(code=create_project, uuid=id_)
        assert res_get_defect.status_code == 200
        assert res_get_defect.body.get("result").get("title") == defect_title

        res_delete = qase.defects.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_update_defects(self, qase, create_project):
        """
        Steps:
        1. Create defects
        2. Update defect
        3. Check response
        """
        defect_title = f"{fake.first_name()} test defect"
        body = {"title": f"{defect_title}", "actual_result": "result", "severity": 1}
        res = qase.defects.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        body_update = {
            "title": f"{defect_title}",
            "actual_result": "result",
            "severity": 1,
        }
        res_update_defect = qase.defects.update(
            code=create_project, uuid=id_, body=body_update
        )
        assert res_update_defect.status_code == 200

        res_delete = qase.defects.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_resolve_defects(self, qase, create_project):
        """
        Steps:
        1. Create defects
        2. Resolve defect
        3. Check response
        """
        defect_title = f"{fake.first_name()} test defect"
        body = {"title": f"{defect_title}", "actual_result": "result", "severity": 1}
        res = qase.defects.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_get_defect = qase.defects.resolve_defect(code=create_project, uuid=id_)
        assert res_get_defect.status_code == 200

        res_delete = qase.defects.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_update_defects_status(self, qase, create_project):
        """
        Steps:
        1. Create defects
        2. Update defect status
        3. Check response
        """
        defect_title = f"{fake.first_name()} test defect"
        body = {"title": f"{defect_title}", "actual_result": "result", "severity": 1}
        res = qase.defects.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        body_update = {"status": "in_progress"}
        res_update_defect = qase.defects.update_status(
            code=create_project, uuid=id_, body=body_update
        )
        assert res_update_defect.status_code == 200

        res_delete = qase.defects.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200
