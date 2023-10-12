import psycopg2
from logger import Logger

class QueryExecutor:
    def __init__(self, db_params):
        self.db_params = db_params
        self.result = None

    def execute_query(self, sql):
        with psycopg2.connect(**self.db_params) as connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    if cursor.description is not None:
                        self.result = cursor.fetchall()
                    else:
                        self.result = None
            except Exception as e:
                connection.rollback()
                raise e
            else:
                connection.commit()
            finally:
                Logger.add_sql_result(self.result)

        return self.result
