import sqlite3
import string
import os

def create_file(file_path, file_name):
    print('Trying to Create Database...')
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    if not os.path.exists(file_name):
        conn = sqlite3.connect(file_name) # setup connection and open file
        cur = conn.cursor()
        # Create table
        cur.execute('''CREATE TABLE game_scripts
                     (NAME,SCRIPT,SECTION)''')
        conn.commit()
        conn.close()
        print('Database created successfully.')
        return True
    else:
        print('File exists. Move on.')
        return False