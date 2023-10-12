import datetime
import os
from requests import Response
from typing import List
from json import JSONDecodeError
import json

class Logger:
    file_name = f"logs/log_" + \
        str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def _write_log_to_file(cls, data: str):
        if not os.path.exists("logs"):
            os.makedirs("logs")
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, data: dict, headers: dict, json: dict, cokies: dict, files: dict, method: str):
        testname = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {testname}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"Request data: {data}\n"
        data_to_add += f"Request files: {files}\n"
        data_to_add += f"Request headers: {headers}\n"
        data_to_add += f"Request cookies: {cokies}\n"
        data_to_add += f"Request json: {json}\n"
        data_to_add += "\n"

        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        headers_as_dict = dict(response.headers)
        cookies_as_dict = dict(response.cookies)

        data_to_add = f"Response code: {response.status_code}\n"
        data_to_add += f"Response text: {response.text}\n"
        data_to_add += f"Response header: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        if len(response.text) == 0:
            data_to_add += f"Response json: Empty response content\n"
        else:
            try:
                data_to_add += f"Response json: {json.dumps(response.json(), indent=4)}\n"
            except JSONDecodeError:
                data_to_add += "Response json: Failed to decode response json\n"

        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_sql_result(cls, result: List[tuple]):
        testname = os.environ.get('PYTEST_CURRENT_TEST')
        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {testname}\n"
        data_to_add += f"SQL result: {result}\n"
        data_to_add += "\n-----\n"
        cls._write_log_to_file(data_to_add)
