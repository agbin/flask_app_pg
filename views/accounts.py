import db
import psycopg2
from flask_app import app
import flask
from flask import json, request
from flask import jsonify
import json



def create_account(name, credits, plan):
    conn = db.pool.getconn()
    with conn.cursor() as cursor:
        try:
            query = 'insert into accounts (client_name, credits, plan) values (%s, %s, %s) returning *'
            cursor.execute(query, (name, credits, plan))
            cursor.connection.commit()
            account = cursor.fetchone()
            return account
        except psycopg2.DatabaseError as e:
            print(e)
            cursor.connection.rollback()
        finally:
            db.pool.putconn(conn)
    return None


@app.route('/accounts', methods=['POST'])
def view_create_account():
    print(flask.request.json)
    name = flask.request.json['client_name']
    credits = flask.request.json['credits']
    plan = flask.request.json['plan']
    create_account(name, credits, plan)
    return flask.jsonify([])


@app.route("/accounts/<int:id>", methods=["GET"])
def account_details(id):
    conn = db.pool.getconn()
    with conn.cursor() as cursor:
        try:
            q = "select * from accounts where id = %s"
            cursor.execute(q, (id,))
            return jsonify({
                "data": str(cursor.fetchall())
            })
        except psycopg2.DatabaseError as e:
            print(e)
            raise e
        finally:
            db.pool.putconn(conn)