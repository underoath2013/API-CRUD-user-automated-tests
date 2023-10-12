from jsonschema import validate


class Response:
    @staticmethod
    def validate(response, schema):
        response_dict = response.json()
        validate(instance=response_dict, schema=schema)

    @staticmethod
    def assert_status_code(response, status_code):
        assert response.status_code == status_code, "Wrong response code"

    @staticmethod
    def assert_content_type(response):
        assert response.headers["Content-Type"] == "application/json", "Content-Type is not application/json"

    @staticmethod
    def assert_json_schema_status_code_content_type(response, status_code, schema):
        Response.validate(response, schema)
        Response.assert_status_code(response, status_code)
        Response.assert_content_type(response)
