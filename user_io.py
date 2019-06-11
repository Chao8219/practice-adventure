import sqlite3
import string
import os
import player_class

def create_file(path, file):
    print('Trying to Create Database...')
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(file):
        conn = sqlite3.connect(file) # setup connection and open file
        cur = conn.cursor()
        # Create table
        cur.execute('''CREATE TABLE players_info
                     (NAME,STR,INT,AGI,DEF,FAI,SAN,LUC,HEAD,ARM,WEAP,FOOT)''')
        conn.commit()
        conn.close()
        print('Database created successfully.')
        return True
    else:
        print('File exists. Move on.')
        return False

def insert_info(player_obj, file):
    """
    Input
    -----
    player_obj: object
    
    file: string

    Return
    ------
    True: insert info into the db file successfully.
    False: insert info into the db file unsuccessfully.
    """
    stre, inte, agi, defe, fai, san, luc = player_obj.attr[0]
    head, body, weap, foot = player_obj.armor
    name = player_obj.name
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    found = find_info(name, file)
    if found == 0:
        formed = ([name, stre, inte, agi, defe, fai, san, luc, 
                    head, body, weap, foot])
        cur.execute('''INSERT INTO players_info
                       VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''', formed)
        conn.commit()
        conn.close()
        print('Database insert successfully')
        return True
    else:
        conn.commit()
        conn.close()
        print('Name exists.')
        return False

def read_one(name, file):
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    cur.execute('SELECT * FROM players_info WHERE NAME=?', (name, ))
    # obtain the player info in a tuple
    fetched_player_info = cur.fetchone()
    player_obj = instan_player(fetched_player_info)
    conn.close()
    print('Database read successfully')
    return player_obj

def instan_player(fetched_info, new_born=False):
    """Instantiate player class from fetched player info"""
    player_obj = player_class.CreatePlayer(fetched_info[0], 
                                            new_born=new_born, 
                                            player_info_list=fetched_info)
    return player_obj

def read_all(file):
    """ This method is to read all info at one time
    It returns a list that contains info.
    It also needs to do empty check before using.
    """
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    cur.execute('SELECT * FROM players_info')
    obtained_all_player_info = cur.fetchall()
    # all players' info store in above variable
    conn.close()
    print('Database read successfully')
    return obtained_all_player_info

def update_info(player_obj, file):
    stre, inte, agi, defe, fai, san, luc = player_obj.attr[0]
    head, body, weap, foot = player_obj.armor
    name = player_obj.name
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    found = find_info(name, file)
    if found is True:
        formed2 = ([stre, inte, agi, defe, fai, san, luc, 
                    head, body, weap, foot, name])
        cur.execute('''UPDATE players_info
                       SET STR=?
                       ,INT=?
                       ,AGI=?
                       ,DEF=?
                       ,FAI=?
                       ,SAN=?
                       ,LUC=?
                       ,HEAD=?
                       ,ARM=?
                       ,WEAP=?
                       ,FOOT=?
                       WHERE NAME= ? ''',formed2)
        conn.commit()
        conn.close()
        print('Database updated successfully')
        return True
    else:
        print('No such file')
        conn.commit()
        conn.close()
        return False

def delete_info(name, file):
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    found = find_info(name, file)
    if found is True:
        cur.execute('''DELETE FROM players_info WHERE NAME = ? ''', 
                (name, ))
        conn.commit()
        print('Data deleted successfully')
        conn.close()
        return True
    else:
        print('No such file')
        conn.commit()
        conn.close()
        return False

def find_info(name, file):
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    cur.execute('''SELECT count(*) FROM players_info WHERE NAME=?''', 
            (name, ))
    data = cur.fetchone()[0]
    if data == 0:
        conn.close()
        return False
    else:
        print('Found it!')
        conn.close()
        return True

def empty_check(file):
    """ This method is to check if the db file is empty or not. 
    It returns True if it is empty.
    It returns False if it is not empty, i.e., there is, at least one 
    saved player in the db file.
    """
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    cur.execute('SELECT * FROM players_info')
    data = cur.fetchall()
    if len(data) == 0:
        print('Empty Table')
        conn.close()
        return True
    else:
        conn.close()
        return False