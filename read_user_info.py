import sqlite3
import string
import os

path='data'
file=path+'/user_info.db'

def create_file():
    print('Trying to Create Database...')
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(file):
        conn=sqlite3.connect(file) # setup connection and open file
        cur = conn.cursor()
        # Create table
        cur.execute('''CREATE TABLE players_info
                     (NAME,STR,INT,AGI,DEF,FAI,SAN,LUC,HEAD,ARM,WEAP,FOOT)''')
        conn.commit()
        conn.close
        print('Database created successfully.')
    else:
        print('File exists. Move on.')
    return

def insert_info(name,stre,inte,agi,defe,fai,san,luc,head,arm,weap,foot):
    conn=sqlite3.connect(file)
    cur = conn.cursor()
    found=find_info(name)
    if(found==0):
        formed=[name,stre,inte,agi,defe,fai,san,luc,head,arm,weap,foot]
        cur.execute('''INSERT INTO players_info
                       VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''',formed)
        conn.commit()
        conn.close
        print('Database insert successfully')
        return 1
    else:
        conn.commit()
        conn.close
        print('Name exists.')
        return 0

def read_info(name):
    global obtained_player_info
    conn=sqlite3.connect(file)
    cur = conn.cursor()
    data=empty_check()
    if(data!=0):
        cur.execute('SELECT * FROM players_info WHERE NAME=?',(name,))
        obtained_player_info=cur.fetchone()
        # this player's info store in above variable
        conn.close
        print('Database read successfully')
        return obtained_player_info
    else:
        conn.close
        return 0

def read_all():
    global obtained_all_player_info
    conn=sqlite3.connect(file)
    cur = conn.cursor()
    data=empty_check()
    if(data!=0):
        cur.execute('SELECT * FROM players_info')
        obtained_all_player_info=cur.fetchall()
        # all players' info store in above variable
        conn.close
        print('Database read successfully')
        return obtained_all_player_info
    else:
        conn.close
        return 0

def update_info(name,stre,inte,agi,defe,fai,san,luc,head,arm,weap,foot):
    conn=sqlite3.connect(file)
    cur = conn.cursor()
    found=find_info(name)
    if(found==1):
        formed2=[stre,inte,agi,defe,fai,san,luc,head,arm,weap,foot,name]
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
        conn.close
        print('Database updated successfully')
        return 1
    else:
        print('No such file')
        conn.commit()
        conn.close
        return 0

def delete_info(name):
    conn=sqlite3.connect(file)
    cur = conn.cursor()
    found=find_info(name)
    if(found==1):
        cur.execute('''DELETE FROM players_info WHERE NAME = ? ''',(name,))
        conn.commit()
        print('Data deleted successfully')
        conn.close
        return 1
    else:
        print('No such file')
        conn.commit()
        conn.close
        return 0

def find_info(name):
    conn=sqlite3.connect(file)
    cur = conn.cursor()
    cur.execute('''SELECT count(*) FROM players_info WHERE NAME=?''',(name,))
    data=cur.fetchone()[0]
    if(data==0):
        conn.close
        return 0
    else:
        print('Found it!')
        conn.close
        return 1

def empty_check():
    conn=sqlite3.connect(file)
    cur = conn.cursor()
    cur.execute('SELECT * FROM players_info')
    data=cur.fetchall()
    if(len(data)==0):
        print('Empty Table')
        conn.close
        return 0
    else:
        conn.close
        return 1

while(1):
    sele=input('1.Read all info\n2.Read only one info by name\n')
    if(sele=='1'):
        ass=read_all()
        formed=['name','stre','inte','agi','defe','fai','san','luc','head','arm','weap','foot']
        for q in range(0,12):
            print(formed[q],end='')
            print(' | ',end='')
        print('')
        for i in range(0,len(ass)):
            for j in range(0,12):
                print(ass[i][j],end='')
                print(' | ',end='')
            print('')
        print('')
    if(sele=='2'):
        sele2=input('Type in one name: ')
        if(find_info(sele2)==1):
            ass2=read_info(sele2)
            formed=['name','stre','inte','agi','defe','fai','san','luc','head','arm','weap','foot']
            for j in range(0,12):
                print(formed[j],end='')
                print(': ',end='')
                print(ass2[j],end='')
                print(' | ',end='')
            print('')
        else:
            print('None such a name exists.\n')
    else:
        print('Please re-select.\n')
