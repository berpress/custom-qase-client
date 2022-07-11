from faker import Faker

fake = Faker()


class TestCustomFields:
    def test_create_custom_fields(self, qase):
        """
        Steps:
        1. Create custom fields
        2. Check response
        """
        body = {"title": f"{fake.first_name()} test title", "entity": 0, "type": 1}
        res = qase.custom_fields.create(body=body)
        assert res.status_code == 200

        res_delete = qase.custom_fields.delete(uuid=res.body.get("result").get("id"))
        assert res_delete.status_code == 200

    def test_get_all_custom_fields(self, qase):
        """
        Steps:
        1. Create custom fields
        2. Get all custom fields
        3. Check response
        """
        field_title = f"{fake.first_name()} test title"
        body = {"title": f"{field_title}", "entity": 0, "type": 1}
        res = qase.custom_fields.create(body=body)
        assert res.status_code == 200

        res_get_all = qase.custom_fields.get_all()
        assert res_get_all.status_code == 200
        results: list = res_get_all.body.get("result").get("entities")
        is_find_field = any(project.get("title") == field_title for project in results)
        assert is_find_field, f"Field {field_title} not found"

        res_delete = qase.custom_fields.delete(uuid=res.body.get("result").get("id"))
        assert res_delete.status_code == 200

    def test_get_custom_field_by_id(self, qase):
        """
        Steps:
        1. Create custom fields
        2. Get custom fields by id
        3. Check response
        """
        field_title = f"{fake.first_name()} test title"
        body = {"title": f"{field_title}", "entity": 0, "type": 1}
        res = qase.custom_fields.create(body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        res_field = qase.custom_fields.get_by_id(uuid=id_)
        assert res_field.status_code == 200
        assert res_field.body.get("result").get("title") == field_title

        res_delete = qase.custom_fields.delete(uuid=id_)
        assert res_delete.status_code == 200

    def test_update_custom_fields(self, qase):
        """
        Steps:
        1. Create custom fields
        2. Update custom fields
        3. Check response
        """
        body = {"title": f"{fake.first_name()} test title", "entity": 0, "type": 1}
        res = qase.custom_fields.create(body=body)
        assert res.status_code == 200
        id_ = res.body.get("result").get("id")

        body_update = {"title": f"{fake.first_name()} test title"}
        res_update = qase.custom_fields.update(uuid=id_, body=body_update)
        assert res_update.status_code == 200

        res_delete = qase.custom_fields.delete(uuid=res.body.get("result").get("id"))
        assert res_delete.status_code == 200
