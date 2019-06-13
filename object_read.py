import sqlite3

def read_all_creature(file_path):
    """
    Method to read all creature data in the creature_info table

    Parameters
    ----------
    file_path: string
        The relative db file path

    Returns
    -------
    all_creature_info: list
        All creature list.
    """
    try:
        conn = sqlite3.connect(file_path)
        cur = conn.cursor()
        cur.execute('SELECT * FROM creature_info')
    except sqlite3.OperationalError as err:
        print(err)
        print('It is possible that the provided file path is wrong.')
        return None
    all_creature_info = cur.fetchall()
    conn.close()
    print('Database read successfully')
    return all_creature_info

def read_one_creature(file_path, creature_name):
    """
    Method to read one creature data by the given creature name.

    Parameters
    ----------
    file_path: string
        The relative db file path

    creature_name: string
        The string name that the code is trying to read.
    
    Returns
    -------
    creature_data: tuple
        The tuple that contains all info about this creature.
    """
    try:
        conn = sqlite3.connect(file_path)
        cur = conn.cursor()
        cur.execute('SELECT * FROM creature_info WHERE NAME=?', 
                    (creature_name, ))
    except sqlite3.OperationalError as err:
        print(err)
        print('It is possible that the provided file path is wrong.')
        return None
    creature_data = cur.fetchone()
    conn.close()
    if creature_data is None:
        print('The creature name that is passed in does not' + 
              'exist in the db file')
    return creature_data