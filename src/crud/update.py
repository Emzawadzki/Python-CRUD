import mysql.connector
from mysql.connector import Error

from globals import connection_config, main_table_name


def update_record():
    record_id = input("Record ID: ")
    if not record_id.isdigit():
        print("Incorrect ID - try INT value!")
        return
    connection = mysql.connector.connect(**connection_config)
    print("[INFO] Connected to MySQL Server")
    cursor = connection.cursor()
    query = "SELECT * FROM " + main_table_name + " WHERE id = %s"
    cursor.execute(query, (record_id,))
    record = cursor.fetchone()
    if record != None:
        _, first_name, last_name = record
        print("Changing " + first_name + " " + last_name + ".")
        new_first_name = input("New first name: ")
        new_last_name = input("New last name: ")
        connection = mysql.connector.connect(**connection_config)
        print("[INFO] Connected to MySQL Server")
        cursor = connection.cursor()
        query = "UPDATE " + main_table_name + \
            " SET first_name = %s, last_name = %s WHERE id = %s"
        values = (new_first_name, new_last_name, record_id)
        cursor.execute(query, values)
        connection.commit()
        print("Record updated!")
    else:
        print("Record with this ID not found!")
    cursor.close()
    connection.close()
    print("[INFO] MySQL connection closed")
