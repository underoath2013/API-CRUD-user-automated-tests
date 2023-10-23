import time
import pytest
from db import users_db_params
from query import QueryExecutor


query_executor_cave = QueryExecutor(users_db_params)


def pytest_configure(config):
    config.addinivalue_line("markers", "timing: mark test for timing")


def pytest_collection_modifyitems(items):
    for item in items:
        if "timing" in item.keywords:
            item.add_marker(pytest.mark.timing)


@pytest.fixture(autouse=True)
def timeit(request):
    start_time = time.time()
    yield
    end_time = time.time()
    test_duration = end_time - start_time
    print(f"Test {request.node.name} took {test_duration:.5f} seconds")


def create_users_table():
    sql = """
        CREATE TABLE IF NOT EXISTS public.users (
        id serial4 NOT NULL,
        name varchar NULL,
        age int4 NULL,
        CONSTRAINT users_pkey PRIMARY KEY (id)
        );
    """
    query_executor_cave.execute_query(sql)


def drop_users_table():
    sql = "DROP TABLE public.users;"
    query_executor_cave.execute_query(sql)


@pytest.fixture(scope="session", autouse=True)
def setup_users_table():
    create_users_table()  # Create table before all tests
    yield
    drop_users_table()  # Delete table after all tests
