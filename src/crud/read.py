import csv

from globals import db_fields, db_file


def read_all_records():
    with open(db_file, "r") as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=db_fields)
        next(reader)
        print("\nDatabase records:")
        for row in reader:
            print(row["first_name"] + " " + row["last_name"])
