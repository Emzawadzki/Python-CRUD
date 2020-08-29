import mysql.connector
from mysql.connector import Error
import flask
from flask import jsonify, request
from flask_cors import CORS

from globals import connection_config, main_table_name
from crud import create, read, update, delete


def prepare_database():
    try:
        connection = mysql.connector.connect(**connection_config)
        if connection.is_connected():
            print("[INFO] Connected to MySQL Server")
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES;")
            table_exists = False
            for tables in cursor:
                if main_table_name in tables:
                    print("[INFO] Table \'" + main_table_name + "\' found!")
                    table_exists = True
            if not table_exists:
                cursor.execute("CREATE TABLE " + main_table_name +
                               " (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255))")
                print("[INFO] Table \'" + main_table_name +
                      "\' was not found and had to be created.")

    except Error as e:
        print("[INFO] Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("[INFO] MySQL connection closed")


# Server start
print("Welcome to PyCRUD!")
prepare_database()

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/api/v1/people', methods=['GET'])
def read_all():
    response = read.read_all_records()
    return jsonify(response)


@app.route('/api/v1/people/<int:person_id>', methods=['GET'])
def read_one(person_id):
    response = read.read_record(person_id)
    return jsonify(response)


@app.route('/api/v1/create', methods=['POST'])
def create_person():
    _json = request.json
    response = create.create_record(_json)
    return jsonify(response)


@app.route('/api/v1/update', methods=['PUT'])
def update_person():
    _json = request.json
    response = update.update_record(_json)
    return jsonify(response)


@app.route('/api/v1/delete/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    response = delete.delete_record(person_id)
    return jsonify(response)


app.run()
