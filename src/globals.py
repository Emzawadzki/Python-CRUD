from credentials import db_user, db_password

db_name = 'py_crud'
main_table_name = 'people'

connection_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'database': db_name,
    'user': db_user,
    'password': db_password,
}
