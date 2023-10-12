import os

users_db_params = {
    "user": os.getenv('POSTGRES_USER', default='postgres'),
    "password": os.getenv('POSTGRES_PASSWORD', default='password'),
    "host":  os.getenv('POSTGRES_HOST', default='localhost'),
    "port": os.getenv('POSTGRES_PORT', default=5432),
    "database": os.getenv('POSTGRES_DB', default='users_db'),

}
