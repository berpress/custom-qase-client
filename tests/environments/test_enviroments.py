from faker import Faker

fake = Faker()


class TestEnv:
    def test_create_env(self, qase, create_project):
        """
        Steps:
        1. Create env
        2. Check response
        """
        env_title = f"{fake.first_name()} test env"
        body = {
            "title": env_title,
            "slug": "test slug",
        }
        res = qase.environments.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_delete = qase.environments.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_get_all_env(self, qase, create_project):
        """
        Steps:
        1. Create env
        2. Get all env
        3. Check response
        """
        env_title = f"{fake.first_name()} test env"
        body = {
            "title": env_title,
            "slug": "test slug",
        }
        res = qase.environments.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_get_all = qase.environments.get_all(code=create_project)
        assert res_get_all.status_code == 200
        results: list = res_get_all.body.get("result").get("entities")
        is_find = any(project.get("title") == env_title for project in results)
        assert is_find, f"Env {env_title} not found"

        res_delete = qase.environments.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_get_specific_env(self, qase, create_project):
        """
        Steps:
        1. Create env
        2. Get specific env
        3. Check response
        """
        env_title = f"{fake.first_name()} test env"
        body = {
            "title": env_title,
            "slug": "test slug",
        }
        res = qase.environments.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_get_env = qase.environments.get_specific_env(code=create_project, uuid=id_)
        assert res_get_env.status_code == 200
        assert res_get_env.body.get("result").get("title") == env_title

        res_delete = qase.environments.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_update_env(self, qase, create_project):
        """
        Steps:
        1. Create env
        2. Update env
        3. Check response
        """
        env_title = f"{fake.first_name()} test env"
        body = {
            "title": env_title,
            "slug": "test slug",
        }
        res = qase.environments.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        body_update = {
            "title": f"{fake.first_name()} test env",
            "slug": "test slug",
        }
        res_update_env = qase.environments.update(
            code=create_project, uuid=id_, body=body_update
        )
        assert res_update_env.status_code == 200

        res_delete = qase.environments.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200
