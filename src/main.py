import mysql.connector
from mysql.connector import Error
import flask
from flask import jsonify, request

from globals import connection_config, main_table_name
from crud import create, read, update, delete

pick_text = "\nPick one of the options below:\n1) Create new record\n2) Read all existing records\n3) Update record by ID\n4) Remove record by ID\nq) Exit\n"
is_running = True


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


# def handle_choice(choice):
#     if choice == "q":
#         global is_running
#         is_running = False
#         print("Closing program ...")
#     elif choice == "1":
#         create.create_record()
#     elif choice == "2":
#         read.read_all_records()
#     elif choice == "3":
#         update.update_record()
#     elif choice == "4":
#         delete.delete_record()
#     else:
#         print("Unknown input.")


# Program start
print("Welcome to PyCRUD!")
prepare_database()

app = flask.Flask(__name__)
app.config["DEBUG"] = True


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
