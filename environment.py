import os


class Environment:
    def get_base_url(self):
        return os.getenv('HOST', default='http://localhost:8000')


ENV_OBJECT = Environment()
