import csv

from globals import db_fields, db_file, db_exists
from crud import create, read


pick_text = "\nPick one of the options below:\n1) Create new record\n2) Read all existing records\nq) Exit"
is_running = True


def initialize_db():
    with open(db_file, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=db_fields)
        writer.writeheader()
    global db_exists
    db_exists = True


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
        print("Unknown input." + pick_text)


# Program start
print("Welcome to PyCRUD!")
if not db_exists:
    print("Database not found. Created new one!")
    initialize_db()
else:
    print("Database found!")

# Main loop
while is_running == True:
    print(pick_text)
    option = input()
    handle_choice(option)
