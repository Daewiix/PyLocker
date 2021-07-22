import pymongo
from decrypt_encrypt_functions import return_chrome_creds
from getpass import getpass
import os
from pymongo.errors import ConfigurationError

def create_db_if_not_exist():
    # create/connect to the database