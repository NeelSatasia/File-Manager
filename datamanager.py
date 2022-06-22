import sqlite3

file_name = '/Users/neel/Documents/Python Projects/File Manager/database.db'

dirs = 'Directories'
ID = 'ID'
dir_name = 'DirName'
dir_path = 'DirPath'
dir_default = 'DefaultDir'
t = 'True'
f = 'False'

def create_database():
    db = sqlite3.connect(file_name)
    cursor = db.cursor()

    query = "CREATE TABLE IF NOT EXISTS {} ({} INTEGER PRIMARY KEY AUTOINCREMENT, {} blob, {} blob, {} text)"
    cursor.execute(query.format(dirs, ID, dir_name, dir_path, dir_default))

    db.commit()
    db.close()


def add_dir_info(dir_nickname, new_dir_path):
    db = sqlite3.connect(file_name)
    cursor = db.cursor()

    query = "INSERT INTO {} values(null, '{}', '{}', '{}')"
    cursor.execute(query.format(dirs, dir_nickname, new_dir_path, f))

    db.commit()
    db.close()


def get_dirs_names():
    db = sqlite3.connect(file_name)
    cursor = db.cursor()

    query = "SELECT {} FROM {}"
    cursor.execute(query.format(dir_name, dirs))

    dirs_names = []

    for dir_info in cursor.fetchall():
        dirs_names.append(dir_info[0])

    db.commit()
    db.close()

    return dirs_names


def remove_dir_directory_list(dir_nickname):
    db = sqlite3.connect(file_name)
    cursor = db.cursor()

    query = "DELETE FROM {} WHERE {} = '{}'"
    cursor.execute(query.format(dirs, dir_name, dir_nickname))

    db.commit()
    db.close()


def get_dir_path(dir_nickname):
    db = sqlite3.connect(file_name)
    cursor = db.cursor()

    query = "SELECT {} FROM {} WHERE {} = '{}'"
    cursor.execute(query.format(dir_path, dirs, dir_name, dir_nickname))

    changed_dir_path = ''

    for value in cursor.fetchall():
        changed_dir_path = value[0]

    query2 = "UPDATE {} SET {} = '{}' WHERE {} = '{}'"
    cursor.execute(query2.format(dirs, dir_default, f, dir_default, t))

    query3 = "UPDATE {} SET {} = '{}' WHERE {} = '{}'"
    cursor.execute(query3.format(dirs, dir_default, t, dir_name, dir_nickname))

    db.commit()
    db.close()

    return changed_dir_path


def get_current_dir_path():
    db = sqlite3.connect(file_name)
    cursor = db.cursor()

    query = "SELECT {} FROM {} WHERE {} = '{}'"
    cursor.execute(query.format(dir_path, dirs, dir_default, t))

    changed_current_dir_path = ''

    for value in cursor.fetchall():
        changed_current_dir_path = value[0]

    db.commit()
    db.close()

    return changed_current_dir_path
