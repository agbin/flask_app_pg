import flask
import db

app = flask.Flask(__name__)
app.config.from_object("config")


db.init_pool(app.config["PG_DSN"],
             app.config["POOL_MINCONN"],
             app.config["POOL_MAXCONN"],
             )