import psycopg2
from psycopg2.pool import ThreadedConnectionPool

pool = None


def init_pool(app):
    global pool
    pool = ThreadedConnectionPool(app.config["POOL_MINCONN"],
                                  app.config["POOL_MAXCONN"],
                                  app.config["PG_DSN"])
