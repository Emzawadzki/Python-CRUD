from credentials import db_user, db_password

db_name = 'py_crud'
db_host = '127.0.0.1'
db_port = 3306

main_table_name = 'people'

connection_config = {
    'host': db_host,
    'port': db_port,
    'database': db_name,
    'user': db_user,
    'password': db_password,
}
