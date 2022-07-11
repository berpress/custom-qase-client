from faker import Faker

fake = Faker()


class TestPlanes:
    def test_create_plane(self, qase, create_project):
        """
        Steps:
        1. Create plane
        2. Check response
        """
        # create case
        body = {"title": "test case"}
        res_case = qase.cases.create(code=create_project, body=body)
        assert res_case.status_code == 200
        assert res_case.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res_case.body.get("result").get("id")

        plane_title = f"{fake.first_name()} test milestone"
        body = {"title": plane_title, "cases": [uuid_case]}
        res = qase.planes.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_delete = qase.planes.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

        res_delete_case = qase.cases.delete(code=create_project, uuid=uuid_case)
        assert res_delete_case.status_code == 200

    def test_get_all_planes(self, qase, create_project):
        """
        Steps:
        1. Create plane
        2. Get all planes
        3. Check response
        """
        # create case
        body = {"title": "test case"}
        res_case = qase.cases.create(code=create_project, body=body)
        assert res_case.status_code == 200
        assert res_case.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res_case.body.get("result").get("id")

        plane_title = f"{fake.first_name()} test milestone"
        body = {"title": plane_title, "cases": [uuid_case]}
        res = qase.planes.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_get_all = qase.planes.get_all(code=create_project)
        assert res_get_all.status_code == 200
        results: list = res_get_all.body.get("result").get("entities")
        is_find = any(project.get("title") == plane_title for project in results)
        assert is_find, f"Plane {plane_title} not found"

        res_delete = qase.planes.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

        res_delete_case = qase.cases.delete(code=create_project, uuid=uuid_case)
        assert res_delete_case.status_code == 200

    def test_get_specific_plane(self, qase, create_project):
        """
        Steps:
        1. Create plane
        2. Get specific plane
        3. Check response
        """
        # create case
        body = {"title": "test case"}
        res_case = qase.cases.create(code=create_project, body=body)
        assert res_case.status_code == 200
        assert res_case.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res_case.body.get("result").get("id")

        plane_title = f"{fake.first_name()} test milestone"
        body = {"title": plane_title, "cases": [uuid_case]}
        res = qase.planes.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_get_env = qase.planes.get_specific_plane(code=create_project, uuid=id_)
        assert res_get_env.status_code == 200
        assert res_get_env.body.get("result").get("title") == plane_title

        res_delete = qase.planes.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

        res_delete_case = qase.cases.delete(code=create_project, uuid=uuid_case)
        assert res_delete_case.status_code == 200

    def test_update_plane(self, qase, create_project):
        """
        Steps:
        1. Create plane
        2. Update plane
        3. Check response
        """
        # create case
        body = {"title": "test case"}
        res_case = qase.cases.create(code=create_project, body=body)
        assert res_case.status_code == 200
        assert res_case.body.get("result").get("id") == 1, "Must be first case"
        uuid_case = res_case.body.get("result").get("id")

        plane_title = f"{fake.first_name()} test milestone"
        body = {"title": plane_title, "cases": [uuid_case]}
        res = qase.planes.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")
        body_update = {
            "title": f"{fake.first_name()} test plane",
        }
        res_update_planes = qase.planes.update(
            code=create_project, uuid=id_, body=body_update
        )
        assert res_update_planes.status_code == 200

        res_delete = qase.planes.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

        res_delete_case = qase.cases.delete(code=create_project, uuid=uuid_case)
        assert res_delete_case.status_code == 200
