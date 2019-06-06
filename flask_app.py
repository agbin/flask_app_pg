import flask
import psycopg2
from psycopg2.pool import ThreadedConnectionPool


app = flask.Flask(__name__)
app.config.from_object("config")

connection_pool = ThreadedConnectionPool(app.config["POOL_MINCONN"],
                                         app.config["POOL_MAXCONN"],
                                         app.config["PG_DSN"])
