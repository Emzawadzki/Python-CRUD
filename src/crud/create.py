import csv

from globals import db_fields, db_file


def create_record():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    with open(db_file, "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=db_fields)
        writer.writerow({'first_name': first_name, 'last_name': last_name})
    print(first_name + last_name + " added to database!")
