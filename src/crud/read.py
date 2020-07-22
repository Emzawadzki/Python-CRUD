import mysql.connector
from mysql.connector import Error

from globals import connection_config, main_table_name


def read_all_records():
    try:
        connection = mysql.connector.connect(**connection_config)
        if connection.is_connected():
            print("[INFO] Connected to MySQL Server")
            cursor = connection.cursor()
            query = "SELECT * FROM " + main_table_name
            cursor.execute(query)
            result = cursor.fetchall()
            for _, first_name, last_name in result:
                print(first_name + " " + last_name)
    except Error as e:
        print("[INFO] Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("[INFO] MySQL connection closed")
