from faker import Faker

fake = Faker()


class TestProjectsAccess:
    def test_grand_access(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Grand access
        3. Check response
        """
        body = {"member_id": 1}
        res = qase.projects.grand_access(code=create_project, body=body)
        assert res.status_code == 400
        assert (
            res.body.get("errorMessage") == "Team member has an access to this "
            "project."
        )
