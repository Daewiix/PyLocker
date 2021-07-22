from decrypt_encrypt_functions import return_chrome_creds
from getpass import getpass
import os
import sqlite3


def insert_row_into_table(origin_url, action_url, username, password):
    try:
        sqliteConnection = sqlite3.connect("password_manager.db")
        cursor = sqliteConnection.cursor()

        sqlite_insert_with_param = """INSERT INTO Logins(origin_url, action_url, username, password) VALUES (?, ?, ?, ?);"""

        data_tuple = (origin_url, action_url, username, password)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def create_table_if_not_exists():
    sqliteConnection = sqlite3.connect("password_manager.db")
    cursor = sqliteConnection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS Logins(origin_url, action_url, username, password)")

    creds = return_chrome_creds()
    for i in creds:
        insert_row_into_table(*i)