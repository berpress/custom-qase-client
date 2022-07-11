class TestAttachments:
    def test_upload_attachments(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Upload attachments
        3. Check response
        """
        res = qase.attachments.upload(create_project, "./cat.jpeg")
        assert res.status_code == 200

        res_delete = qase.attachments.remove_by_hash(
            hash=res.body.get("result")[0].get("hash")
        )
        assert res_delete.status_code == 200

    def test_get_all_attachments(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Upload attachments
        3. Get all attachments
        4. Check response
        """
        res = qase.attachments.upload(create_project, "./cat.jpeg")
        assert res.status_code == 200

        res_attachments = qase.attachments.get_all()
        assert res_attachments.status_code == 200

        res_delete = qase.attachments.remove_by_hash(
            hash=res.body.get("result")[0].get("hash")
        )
        assert res_delete.status_code == 200

    def test_get_attachments_by_uuid(self, qase, create_project):
        """
        Steps:
        1. Create new project
        2. Upload attachments
        3. Get attachments by hash
        3. Check response
        """
        res = qase.attachments.upload(create_project, "./cat.jpeg")
        assert res.status_code == 200

        res_get = qase.attachments.get_by_hash(
            hash=res.body.get("result")[0].get("hash")
        )
        assert res_get.status_code == 200

        res_delete = qase.attachments.remove_by_hash(
            hash=res.body.get("result")[0].get("hash")
        )
        assert res_delete.status_code == 200
