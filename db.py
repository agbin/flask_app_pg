import psycopg2
from psycopg2.pool import ThreadedConnectionPool

pool = None


def init_pool(dsn, minconn=3, maxconn=7):
    global pool
    pool = ThreadedConnectionPool(minconn, maxconn, dsn)
