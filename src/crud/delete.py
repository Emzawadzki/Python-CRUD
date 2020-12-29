import mysql.connector

from globals import connection_config, main_table_name
from res_creator import create_response, create_error


def delete_record(person_id):
    connection = mysql.connector.connect(**connection_config)
    print("[INFO] Connected to MySQL Server")
    cursor = connection.cursor()

    select_query = "SELECT EXISTS(SELECT * FROM " + \
        main_table_name + " WHERE id = %s)"
    cursor.execute(select_query, (person_id,))
    (is_exist,) = cursor.fetchone()
    if is_exist == 0:
        cursor.close()
        connection.close()
        return create_error("person_id_not_found")
    delete_query = "DELETE FROM " + main_table_name + " WHERE id = %s"
    cursor.execute(delete_query, (person_id,))
    connection.commit()
    print("Record removed!")
    cursor.close()
    connection.close()
    print("[INFO] MySQL connection closed")
    return create_response(None)
