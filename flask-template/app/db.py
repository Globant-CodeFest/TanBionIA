import psycopg2
import psycopg2.extras
from flask import current_app
from flask import g


def connection():
    if "db_conn" not in g:
        conf = current_app.config
        g.db_conn = psycopg2.connect(
            host=conf["DB_HOST"],
            user=conf["DB_USER"],
            password=conf["DB_PASS"],
            dbname=conf["DB_NAME"],
            cursor_factory=psycopg2.extras.RealDictCursor,  # https://www.psycopg.org/docs/extras.html#psycopg2.extras.DictCursor
        )

    return g.db_conn


def close(e=None):
    conn = g.pop("db_conn", None)

    if conn is not None:
        conn.close()


def init_app(app):
    app.teardown_appcontext(close)
