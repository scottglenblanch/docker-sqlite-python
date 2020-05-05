import sqlite3
from database_interaction import run_sql


def create_user_table():
    run_sql('''CREATE TABLE IF NOT EXISTS user
        (user_id integer primary key, user_name text, user_email text)''')


def import_data_to_user_table():
    data_to_import = [
        {'user_name': 'person1', 'user_email': 'person1@someemail.com'},
        {'user_name': 'person2', 'user_email': 'person2@someemail.com'}
    ]

    for o in data_to_import:
        user_name = o['user_name']
        user_email = o['user_email']
        run_sql("INSERT INTO user(user_name, user_email) VALUES ('{0}', '{1}')".format(user_name, user_email))
