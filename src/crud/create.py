import mysql.connector

from globals import connection_config, main_table_name
from res_creator import create_response, create_error


def create_record(request):
    if "first_name" not in request:
        return create_error("first_name_required")
    if "last_name" not in request:
        return create_error("last_name_required")
    first_name = request["first_name"]
    last_name = request["last_name"]
    connection = mysql.connector.connect(**connection_config)
    print("[INFO] Connected to MySQL Server")
    cursor = connection.cursor()
    query = "INSERT INTO " + main_table_name + \
        " (first_name, last_name) VALUES (%s, %s)"
    values = (first_name, last_name)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    print(first_name + " " + last_name + " added to database!")
    print("[INFO] MySQL connection closed")
    return create_response(None)
