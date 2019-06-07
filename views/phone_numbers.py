import psycopg2
from flask import jsonify
from flask_app import app
import db


@app.route("/phone_numbers", methods=["GET"])
def list_all():
    conn = db.pool.getconn()
    with conn.cursor() as cursor:
        try:
            cursor.execute("select * from phone_numbers")
            return jsonify(cursor.fetchall())
        except psycopg2.DatabaseError as e:
            print(e)
        finally:
            db.pool.putconn(conn)


@app.route("/phone_numbers/<string:phone_number>", methods=["GET"])
def phone_number_details(phone_number):
    conn = db.pool.getconn()
    with conn.cursor() as cursor:
        try:
            q = "select * from phone_numbers where phone_number = %s"
            cursor.execute(q, (phone_number,))
            return jsonify({
                "data": cursor.fetchall()
            })
        except psycopg2.DatabaseError as e:
            print(e)
            raise e
        finally:
            db.pool.putconn(conn)
