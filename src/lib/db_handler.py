from .decrypt_encrypt_functions import return_chrome_creds
from getpass import getpass
from sqlite3 import OperationalError
import os
import sqlite3
import json

class Handler:
    def __init__(self, path: str) -> None:
        """Initialize function to run when object is created for the class

        Args
            path (str): Path to the database
        """
        self.path = path
        self.password_manager_db = "password_manager.db"
        self.chrome_db_copy = "chrome_data.db"
        with open("setup.json", "r+") as f:
            self.data = json.load(f)

    def insert_row_into_table(self, origin_url: str, action_url: str, username: str, password: str) -> None:
        """Add row into the table just for ease of use

        Args:
            origin_url (str): URL
            action_url (str): Executed url
            username_url (str): Username
            password_url (str): Password
        """
        try:
            sqliteConnection = sqlite3.connect(os.path.join(self.path, self.password_manager_db))
            cursor = sqliteConnection.cursor()

            sqlite_insert_with_param = """INSERT INTO Logins(origin_url, action_url, username, password) VALUES (?, ?, ?, ?);"""
            cursor.execute(sqlite_insert_with_param, (origin_url, action_url, username, password))
            sqliteConnection.commit()

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()

    def create_db_if_not_exists(self) -> None:
        """Create a database if it does not exist"""
        if self.data == False:
            sqliteConnection = sqlite3.connect(os.path.join(self.path, self.password_manager_db))
            cursor = sqliteConnection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS Logins(origin_url, action_url, username, password)")
            creds = return_chrome_creds(os.path.join(self.path, self.chrome_db_copy))
            for i in creds:
                self.insert_row_into_table(*i)
        else:
            os.mkdir(self.path)