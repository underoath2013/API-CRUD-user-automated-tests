import allure
import pytest
from my_requests import MyRequests
from basic_assertions import Response
from schemas.user_schema import user_schema
from schemas.error_schema import error_schema
from fake_data import FakeData

error_message_str = "str type expected"
error_message_str_min_length = "ensure this value has at least 1 characters"
error_message_str_max_length = "ensure this value has at most 100 characters"
error_message_int = "value is not a valid integer"
error_message_int_min_value = "ensure this value is greater than or equal to 0"
error_message_int_max_value = "ensure this value is less than or equal to 100"
error_required_field = "field required"

@allure.epic("User test cases")
class TestUser:

    def test_get_get_all_users_200(self):
        response = MyRequests.get(f'/user')
        Response.assert_json_schema_status_code_content_type(response, 200, user_schema)

    @pytest.mark.parametrize('name, age',
                             [   # create 2 valid users
                                 (FakeData.name(), FakeData.age()),
                                 (FakeData.name(), FakeData.age())
                             ]
                             )
    def test_post_create_user_200(self, name, age):
        data = {
            "name": name,
            "age": age
        }
        response = MyRequests.post(f"/user/create", json=data)
        Response.assert_json_schema_status_code_content_type(response, 200, user_schema)

    def test_get_get_all_created_users_200(self):
        response = MyRequests.get(f'/user')
        response_dict = response.json()
        Response.assert_json_schema_status_code_content_type(response, 200, user_schema)
        for item in response_dict["result"]:
            assert all(key in item for key in ("name", "age", "id")), 'Not all keys ("name", "age", "id") in result'

    @pytest.mark.parametrize('name, age',
                             [   # not valid name
                                 ("", FakeData.age()),
                                 (FakeData.big_string(), FakeData.age()),
                                 (FakeData.random_int(), FakeData.age())
                             ]
                             )
    def test_post_create_user_not_valid_name_422(self, name, age):
        data = {
            "name": name,
            "age": age
        }
        response = MyRequests.post(f"/user/create", json=data)
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)

    @pytest.mark.parametrize('name, age',
                             [   # not valid age
                                 (FakeData.name(), FakeData.random_string()),
                                 (FakeData.name(), -1),
                                 (FakeData.name(), 101)
                             ]
                             )
    def test_post_create_user_not_valid_age_422(self, name, age):
        data = {
            "name": name,
            "age": age
        }
        response = MyRequests.post(f"/user/create", json=data)
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)

    def test_post_create_user_with_no_required_body_422(self):
        response = MyRequests.post("/user/create")
        response_dict = response.json()
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)
        assert response_dict["detail"][0]["msg"] == error_required_field, "Wrong error message"

    def test_post_create_user_name_empty_key_422(self):
        data = {"": FakeData.name(), "age": FakeData.age()}
        response = MyRequests.post("/user/create", json=data)
        response_dict = response.json()
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)
        assert response_dict["detail"][0]["msg"] == error_required_field, "Wrong error message"

    def test_post_create_user_age_empty_key_422(self):
        data = {"name": FakeData.name(), "": FakeData.age()}
        response = MyRequests.post("/user/create", json=data)
        response_dict = response.json()
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)
        assert response_dict["detail"][0]["msg"] == error_required_field, "Wrong error message"

    @pytest.fixture(scope="function")
    def user_id(self):
        response = MyRequests.get(f'/user')
        response_dict = response.json()
        Response.assert_json_schema_status_code_content_type(response, 200, user_schema)
        ids = [item["id"] for item in response_dict["result"]]
        user_id = ids[0]
        return user_id

    def test_delete_user_by_id_200(self, user_id):
        response = MyRequests.delete(f'/user/{user_id}')
        Response.assert_json_schema_status_code_content_type(response, 200, user_schema)

    def test_delete_user_by_fake_id_200(self):
        response = MyRequests.delete(f'/user/{FakeData.random_int()}')
        Response.assert_json_schema_status_code_content_type(response, 404, error_schema)

    def test_delete_user_not_valid_user_id_path_422(self):
        response = MyRequests.delete(f'/user/text')
        response_dict = response.json()
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)
        assert response_dict["detail"][0]["msg"] == error_message_int, "Wrong error message"

    def test_get_user_by_id_200(self, user_id):
        response = MyRequests.get(f'/user/{user_id}')
        Response.assert_json_schema_status_code_content_type(response, 200, user_schema)

    def test_get_user_by_fake_id_200(self):
        response = MyRequests.get(f'/user/{FakeData.random_int()}')
        Response.assert_json_schema_status_code_content_type(response, 404, error_schema)

    def test_get_user_not_valid_user_id_path_422(self):
        response = MyRequests.get(f'/user/text')
        response_dict = response.json()
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)
        assert response_dict["detail"][0]["msg"] == error_message_int, "Wrong error message"

    @pytest.mark.parametrize('name, age',
                             [   # update user
                                 (FakeData.name(), FakeData.age()),
                                 (FakeData.name(), FakeData.age())
                             ]
                             )
    def test_put_update_user_200(self, user_id, name, age):
        data = {
            "name": name,
            "age": age
        }
        response = MyRequests.put(f"/user/{user_id}", json=data)
        Response.assert_json_schema_status_code_content_type(response, 200, user_schema)

    @pytest.mark.parametrize('name, age',
                             [   # not valid name
                                 ("", FakeData.age()),
                                 (FakeData.big_string(), FakeData.age()),
                                 (FakeData.random_int(), FakeData.age())
                             ]
                             )
    def test_put_update_user_not_valid_name_422(self, user_id, name, age):
        data = {
            "name": name,
            "age": age
        }
        response = MyRequests.put(f"/user/{user_id}", json=data)
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)

    @pytest.mark.parametrize('name, age',
                             [   # not valid age
                                 (FakeData.name(), FakeData.random_string()),
                                 (FakeData.name(), -1),
                                 (FakeData.name(), 101)
                             ]
                             )
    def test_put_update_user_not_valid_age_422(self, user_id, name, age):
        data = {
            "name": name,
            "age": age
        }
        response = MyRequests.put(f"/user/{user_id}", json=data)
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)

    def test_put_update_user_with_no_required_body_422(self, user_id):
        response = MyRequests.put(f'/user/{user_id}')
        response_dict = response.json()
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)
        assert response_dict["detail"][0]["msg"] == error_required_field, "Wrong error message"

    def test_put_update_user_name_empty_key_422(self, user_id):
        data = {"": FakeData.name(), "age": FakeData.age()}
        response = MyRequests.put(f'/user/{user_id}', json=data)
        response_dict = response.json()
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)
        assert response_dict["detail"][0]["msg"] == error_required_field, "Wrong error message"

    def test_put_update_user_age_empty_key_422(self, user_id):
        data = {"name": FakeData.name(), "": FakeData.age()}
        response = MyRequests.put(f'/user/{user_id}', json=data)
        response_dict = response.json()
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)
        assert response_dict["detail"][0]["msg"] == error_required_field, "Wrong error message"

    def test_put_update_user_by_fake_id_404(self):
        data = {"name": FakeData.name(), "age": FakeData.age()}
        response = MyRequests.put(f'/user/{FakeData.random_int()}', json=data)
        Response.assert_json_schema_status_code_content_type(response, 404, error_schema)

    def test_put_update_user_not_valid_user_id_path_422(self):
        data = {"name": FakeData.name(), "age": FakeData.age()}
        response = MyRequests.put(f'/user/text', json=data)
        response_dict = response.json()
        Response.assert_json_schema_status_code_content_type(response, 422, error_schema)
        assert response_dict["detail"][0]["msg"] == error_message_int, "Wrong error message"
