import mysql.connector

from globals import connection_config, main_table_name


def read_all_records():
    connection = mysql.connector.connect(**connection_config)
    print("[INFO] Connected to MySQL Server")
    cursor = connection.cursor()
    query = "SELECT * FROM " + main_table_name
    cursor.execute(query)
    result = cursor.fetchall()
    for _, first_name, last_name in result:
        print(first_name + " " + last_name)
    cursor.close()
    connection.close()
    print("[INFO] MySQL connection closed")
