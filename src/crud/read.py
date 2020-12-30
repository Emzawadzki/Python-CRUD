import mysql.connector
from flask_api import status
from globals import connection_config, main_table_name
from res_creator import create_response, create_error


def read_all_records():
    connection = mysql.connector.connect(**connection_config)
    print("[INFO] Connected to MySQL Server")
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM " + main_table_name
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    print("[INFO] MySQL connection closed")
    return create_response(rows)


def read_record(person_id):
    connection = mysql.connector.connect(**connection_config)
    print("[INFO] Connected to MySQL Server")
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM " + main_table_name + " WHERE id = %s"
    cursor.execute(query, (person_id,))
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    print("[INFO] MySQL connection closed")
    if row is None:
        return create_error("person_not_found", status.HTTP_404_NOT_FOUND)
    return create_response(row)
