import os.path

db_fields = ['first_name', 'last_name']
db_file = 'database.csv'
db_exists = os.path.isfile(db_file)
