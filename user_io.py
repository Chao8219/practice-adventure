import sqlite3
import string
import os

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

def insert_info(name, attr, armor, file):
    stre, inte, agi, defe, fai, san, luc = attr[0] # unpack it
    head, body, weap, foot = armor
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    found = find_info(name, file)
    if found == 0:
        formed=[name,stre,inte,agi,defe,fai,san,luc,head,body,weap,foot]
        cur.execute('''INSERT INTO players_info
                       VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''', formed)
        conn.commit()
        conn.close()
        print('Database insert successfully')
        return 1
    else:
        conn.commit()
        conn.close()
        print('Name exists.')
        return 0

def read_info(name, file):
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    data = empty_check(file)
    if data != 0:
        cur.execute('SELECT * FROM players_info WHERE NAME=?', (name, ))
        obtained_player_info = cur.fetchone()
        # this player's info store in above variable
        conn.close()
        print('Database read successfully')
        return obtained_player_info
    else:
        conn.close()
        return 0

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

def update_info(name, attr, armor, file):
    stre, inte, agi, defe, fai, san, luc = attr[0] # unpack it
    head, body, weap, foot = armor
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    found = find_info(name, file)
    if found == 1:
        formed2=[stre,inte,agi,defe,fai,san,luc,head,body,weap,foot,name]
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
        return 1
    else:
        print('No such file')
        conn.commit()
        conn.close()
        return 0

def delete_info(name, file):
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    found = find_info(name, file)
    if found == 1:
        cur.execute('''DELETE FROM players_info WHERE NAME = ? ''', 
                (name, ))
        conn.commit()
        print('Data deleted successfully')
        conn.close()
        return 1
    else:
        print('No such file')
        conn.commit()
        conn.close()
        return 0

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