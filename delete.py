import sqlite3

conn = sqlite3.connect("password_manager.db")
cursor = conn.cursor()

cursor.execute("""DROP TABLE contacts""")
cursor.connection.commit()
