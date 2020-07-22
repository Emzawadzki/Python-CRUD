import mysql.connector

from globals import connection_config, main_table_name


def create_record():
    first_name = input("First name: ")
    last_name = input("Last name: ")
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
    print(first_name + last_name + " added to database!")
    print("[INFO] MySQL connection closed")
