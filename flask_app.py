import flask
import db
from decimal import Decimal
import json
from datetime import datetime


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, datetime):
            return obj.ctime()
        return json.JSONEncoder.default(self, obj)


app = flask.Flask(__name__)
app.config.from_object("config")
app.json_encoder = JsonEncoder


db.init_pool(app.config["PG_DSN"],
             app.config["POOL_MINCONN"],
             app.config["POOL_MAXCONN"],
             )
