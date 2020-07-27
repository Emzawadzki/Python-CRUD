import mysql.connector
from getch import getch

from globals import connection_config, main_table_name


def prompt_delete(record):
    if record == None:
        print("Record with this ID not found!")
        return
    id, first_name, last_name = record
    print("Removing " + first_name + " " + last_name + ". Are you sure?")
    while True:
        print("Type y/n to confirm.")
        char = getch()
        if char == 'y':
            break
        elif char == 'n':
            should_remove = False
            return
        else:
            print("Incorrect input!")
    connection = mysql.connector.connect(**connection_config)
    print("[INFO] Connected to MySQL Server")
    cursor = connection.cursor()
    query = "DELETE FROM " + main_table_name + " WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    print("Record removed!")


def delete_record():
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
    prompt_delete(record)
    cursor.close()
    connection.close()
    print("[INFO] MySQL connection closed")
