import mysql.connector

from globals import connection_config, main_table_name


def read_all_records():
    connection = mysql.connector.connect(**connection_config)
    print("[INFO] Connected to MySQL Server")
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM " + main_table_name
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    print("[INFO] MySQL connection closed")
    return result
