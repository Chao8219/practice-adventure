import sqlite3

def read_all_creature():
    file_path = '../data/object_info.db'
    conn = sqlite3.connect(file_path)
    cur = conn.cursor()
    cur.execute('SELECT * FROM creature_info')
    all_creature_info = cur.fetchall()
    conn.close()
    print('Database read successfully')
    return all_creature_info