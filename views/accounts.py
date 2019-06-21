import db
import psycopg2
from flask_app import app
import flask
from flask import jsonify


def create_account(name, credits, plan):
    conn = db.pool.getconn()
    with conn.cursor() as cursor:
        try:
            query = (
                'insert into accounts (client_name, credits, plan)'
                '  values (%bs, %s, %s) returning *'
            )
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


def account_details(id):
    conn = db.pool.getconn()
    with conn.cursor() as cursor:
        try:
            q = "select * from accounts where id = %s"
            cursor.execute(q, (id,))
            record = dict(cursor.fetchone() or {})
            return record
        except psycopg2.DatabaseError as e:
            print(e)
            raise e
        finally:
            db.pool.putconn(conn)


def account_remove(id):
    conn = db.pool.getconn()
    with conn.cursor() as cursor:
        try:
            q = "delete from accounts where id = %s"
            cursor.execute(q, (id,))
            cursor.connection.commit()
            return "The account has been removed"
        except psycopg2.DatabaseError as e:
            print(e)
            raise e
        finally:
            db.pool.putconn(conn)


def update_account(name, credits, plan, id):
    conn = db.pool.getconn()
    with conn.cursor() as cursor:
        try:
            query = 'update accounts set client_name = %s, credits = %s, plan = %s where id = %s returning *'
            cursor.execute(query, (name, credits, plan, id))
            account = cursor.fetchone()
            if not account:
                flask.abort(404)
            cursor.connection.commit()
            return jsonify(dict(account))

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
    account = create_account(name, credits, plan)
    return flask.jsonify(account)


@app.route("/accounts/<int:id>", methods=['GET'])
def view_show_account(id):
    return jsonify({'data': account_details(id)})


@app.route("/accounts/<int:id>", methods=['DELETE'])
def view_remove_account(id):
    return account_remove(id)


@app.route("/accounts/<int:id>", methods=['PATCH'])
def view_modify_account(id):
    name = flask.request.json['client_name']
    credits = flask.request.json['credits']
    plan = flask.request.json['plan']
    return update_account(name, credits, plan, id)
