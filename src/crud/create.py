import csv
import os.path

db_fields = ['first_name', 'last_name']
db_file = 'database.csv'
db_exists = os.path.isfile(db_file)


def initialize_db():
    with open(db_file, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=db_fields)
        writer.writeheader()
    global db_exists
    db_exists = True


def create_record():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    if not db_exists:
        initialize_db()

    with open(db_file, "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=db_fields)
        writer.writerow({'first_name': first_name, 'last_name': last_name})
    print(first_name + last_name + " added to database!\n")
