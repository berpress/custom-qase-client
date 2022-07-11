from faker import Faker

fake = Faker()


class TestMilestones:
    def test_create_milestones(self, qase, create_project):
        """
        Steps:
        1. Create milestones
        2. Check response
        """
        milestone_title = f"{fake.first_name()} test milestone"
        body = {
            "title": milestone_title,
        }
        res = qase.milestones.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_delete = qase.milestones.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_get_all_milestone(self, qase, create_project):
        """
        Steps:
        1. Create env
        2. Get all milestone
        3. Check response
        """
        milestone_title = f"{fake.first_name()} test milestone"
        body = {
            "title": milestone_title,
        }
        res = qase.milestones.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_get_all = qase.milestones.get_all(code=create_project)
        assert res_get_all.status_code == 200
        results: list = res_get_all.body.get("result").get("entities")
        is_find = any(project.get("title") == milestone_title for project in results)
        assert is_find, f"Milestone {milestone_title} not found"

        res_delete = qase.milestones.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_get_specific_env(self, qase, create_project):
        """
        Steps:
        1. Create milestones
        2. Get specific milestones
        3. Check response
        """
        milestone_title = f"{fake.first_name()} test milestone"
        body = {
            "title": milestone_title,
            "slug": "test slug",
        }
        res = qase.milestones.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_get_env = qase.milestones.get_specific_milestone(
            code=create_project, uuid=id_
        )
        assert res_get_env.status_code == 200
        assert res_get_env.body.get("result").get("title") == milestone_title

        res_delete = qase.milestones.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200

    def test_update_milestones(self, qase, create_project):
        """
        Steps:
        1. Create milestones
        2. Update milestones
        3. Check response
        """
        milestone_title = f"{fake.first_name()} test milestone"
        body = {
            "title": milestone_title,
        }
        res = qase.milestones.create(code=create_project, body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        body_update = {
            "title": f"{fake.first_name()} test milestone",
        }
        res_update_milestones = qase.milestones.update(
            code=create_project, uuid=id_, body=body_update
        )
        assert res_update_milestones.status_code == 200

        res_delete = qase.milestones.delete(code=create_project, uuid=id_)
        assert res_delete.status_code == 200
