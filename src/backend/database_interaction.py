import sqlite3
db_file_path = '/app/db/mydatabase.db'


def run_sql(sql_script):
    conn = sqlite3.connect(db_file_path)

    cursor = conn.cursor()
    cursor.execute(sql_script)

    conn.commit()
    conn.close()
