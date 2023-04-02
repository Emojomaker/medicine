import os
import contextlib
import psycopg2


@contextlib.contextmanager
def get_postgresql_conn(host, db_name, user, pwd):
    conn = psycopg2.connect(host=host,
                            database=db_name,
                            user=user,
                            password=pwd)
    return conn
    try:
        yield conn
    finally:
        conn.close()