import mysql.connector
from mysql.connector import Error

from globals import connection_config, main_table_name
from crud import create, read

pick_text = "\nPick one of the options below:\n1) Create new record\n2) Read all existing records\nq) Exit"
is_running = True


def prepare_database():
    try:
        connection = mysql.connector.connect(**connection_config)
        if connection.is_connected():
            print("[INFO] Connected to MySQL Server")
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES;")
            table_exists = False
            for tables in cursor:
                if main_table_name in tables:
                    print("[INFO] Table \'" + main_table_name + "\' found!")
                    table_exists = True
            if not table_exists:
                cursor.execute("CREATE TABLE " + main_table_name +
                               " (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255))")
                print("[INFO] Table \'" + main_table_name +
                      "\' was not found and had to be created.")

    except Error as e:
        print("[INFO] Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("[INFO] MySQL connection closed")


def handle_choice(choice):
    if choice == "q":
        global is_running
        is_running = False
        print("Closing program ...")
    elif choice == "1":
        create.create_record()
    elif choice == "2":
        read.read_all_records()
    else:
        print("Unknown input.")


# Program start
print("Welcome to PyCRUD!")
prepare_database()

# Main loop
while is_running == True:
    print(pick_text)
    option = input()
    handle_choice(option)
