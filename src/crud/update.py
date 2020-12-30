import mysql.connector
from flask_api import status
from globals import connection_config, main_table_name
from res_creator import create_response, create_error


def update_record(person_id, request):
    first_name = None
    last_name = None
    if "first_name" in request:
        first_name = request["first_name"]
    if "last_name" in request:
        last_name = request["last_name"]
    if first_name is None and last_name is None:
        return create_error("field_to_update_required", status.HTTP_400_BAD_REQUEST)

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
        return create_error("person_id_not_found", status.HTTP_404_NOT_FOUND)

    update_query = "UPDATE " + main_table_name + " SET "
    updated_fields = []
    if first_name is not None:
        updated_fields.append("first_name = '" + first_name + "'")
    if last_name is not None:
        updated_fields.append("last_name = '" + last_name + "'")
    update_query += ', '.join(updated_fields)
    update_query += " WHERE id = %s"
    print("Update query: ", update_query)
    cursor.execute(update_query, (person_id,))
    connection.commit()
    print("Record updated!")

    cursor.close()
    connection.close()
    print("[INFO] MySQL connection closed")

    return create_response(None)
