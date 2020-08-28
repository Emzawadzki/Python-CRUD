import mysql.connector

from globals import connection_config, main_table_name
from res_creator import create_response, create_error


def update_record(request):
    person_id = None
    first_name = None
    last_name = None
    if "id" in request:
        person_id = request["id"]
    else:
        return create_error("person_id_required")
    if "first_name" in request:
        first_name = request["first_name"]
    else:
        return create_error("first_name_required")
    if "last_name" in request:
        last_name = request["last_name"]
    else:
        return create_error("last_name_required")

    connection = mysql.connector.connect(**connection_config)
    print("[INFO] Connected to MySQL Server")
    cursor = connection.cursor()
    query = "SELECT EXISTS(SELECT * FROM " + \
        main_table_name + " WHERE id = %s)"
    cursor.execute(query, (person_id,))
    (is_exist,) = cursor.fetchone()
    if is_exist == 0:
        cursor.close()
        connection.close()
        return create_error("person_id_not_found")

    query = "UPDATE " + main_table_name + \
        " SET first_name = %s, last_name = %s WHERE id = %s"
    values = (first_name, last_name, person_id)
    cursor.execute(query, values)
    connection.commit()
    print("Record updated!")

    cursor.close()
    connection.close()
    print("[INFO] MySQL connection closed")

    return create_response(None)
