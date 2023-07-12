import psycopg2
from flask import g

DEV_CONN_PARAMS = {
    "host": "localhost",
    "port": 5432,
    "dbname": "newDb",
    "user": "postgres",
    "password": "saif"
}

CONN_PARAMS = DEV_CONN_PARAMS
connection_string = f"postgresql://{CONN_PARAMS['user']}:{CONN_PARAMS['password']}@{CONN_PARAMS['host']}:{CONN_PARAMS['port']}/{CONN_PARAMS['dbname']}"

def get_db_conn():
    db_conn = getattr(g, '_db_conn', None)
    if db_conn is None:
        db_conn = g._db_conn = psycopg2.connect(connection_string)
    return db_conn