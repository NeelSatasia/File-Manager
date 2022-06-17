import sqlite3

file_name = 'database.db'

ID = 'ID'
dir_name = 'Directory Name'
dir_path = 'Directory Path'
dir_default = 'Default'

def create_database():
    db = sqlite3.connect(file_name)
    cursor = db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS " + accounts + "(" + ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + dir_name + " text, " + dir_path + " text, " + dir_default + " text)")

    db.commit()
    db.close()
