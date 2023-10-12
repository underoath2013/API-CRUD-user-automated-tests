import requests
from logger import Logger
from environment import ENV_OBJECT


class MyRequests():
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, json: dict = None, cookies=None, files=None):
        return MyRequests._send(url, data, headers, json, cookies, files, "POST")

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, json: dict = None, cookies=None, files=None):
        return MyRequests._send(url, data, headers, json, cookies, files, "GET")

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, json: dict = None, cookies=None, files=None):
        return MyRequests._send(url, data, headers, json, cookies, files, "PUT")

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, json: dict = None, cookies=None, files=None):
        return MyRequests._send(url, data, headers, json, cookies, files, "DELETE")

    @staticmethod
    def _send(url: str, data: dict, headers: dict, json: dict, cookies: dict, files: dict, method: str):

        url = f"{ENV_OBJECT.get_base_url()}{url}"

        if headers is None:
            headers = {}
        if data is None:
            data = {}
        if json is None:
            json = None
        if cookies is None:
            cookies = {}
        if files is None:
            files = {}

        Logger.add_request(url, data, headers, json, cookies, files, method)

        if method == 'GET':
            response = requests.get(
                url, params=data, headers=headers, json=json, cookies=cookies, files=files)
        elif method == 'POST':
            response = requests.post(
                url, data=data, headers=headers, json=json, cookies=cookies, files=files)
        elif method == 'PUT':
            response = requests.put(
                url, data=data, headers=headers, json=json, cookies=cookies, files=files)
        elif method == 'DELETE':
            response = requests.delete(
                url, data=data, headers=headers, json=json, cookies=cookies, files=files)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        Logger.add_response(response)

        return response
