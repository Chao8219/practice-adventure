import sqlite3
import string
import os

path='userinfo'
file=path+'/sqlite3_test.db'

def create_file():
    print('Trying to Create Database...')
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(file):
        conn=sqlite3.connect(file) # setup connection and open file
        cur = conn.cursor()
        # Create table
        cur.execute('''CREATE TABLE players_info
                     (ID,NAME,CHARACTER,OTH)''')
        conn.commit()
        conn.close
        print('Database created successfully.')
    else:
        print('File exists. Move on.')
    return

def insert_info(ID_insert,name_insert,character_insert,other):
    conn=sqlite3.connect(file)
    cur = conn.cursor()
    found=find_info(name_insert)
    if(found==0):
        formed=[ID_insert,name_insert,character_insert,other]
        cur.execute('''INSERT INTO players_info
                       VALUES(?,?,?,?)''',formed)
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
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    data = empty_check()
    if(data!=0):
        cur.execute('SELECT * FROM players_info WHERE NAME=?',(name,))
        cool=cur.fetchone()
        print(cool)
        conn.close
        print('Database read successfully')
        return 1
    else:
        conn.close
        return 0
    
def read_all():
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    data = empty_check()
    if(data!=0):
        #for row in cur.execute('SELECT * FROM players_info'):
        #    print(row)
        cur.execute('SELECT * FROM players_info')
        ass=cur.fetchall()
        for j in range(0,len(ass)):
            print(ass[j][0]+' | '+ass[j][1]+' | '+ass[j][2]+' | '+ass[j][3])
        conn.close
        print('Database read successfully')
        return 1
    else:
        conn.close
        return 0

def update_info(name_insert,character_insert,other):
    conn=sqlite3.connect(file)
    cur = conn.cursor()
    found=find_info(name_insert)
    if(found==1):
        formed2=[character_insert,other,name_insert]
        cur.execute('''UPDATE players_info
                       SET CHARACTER=?
                       ,OTH=?
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

def delete_info(name_insert):
    conn=sqlite3.connect(file)
    cur = conn.cursor()
    found=find_info(name_insert)
    if(found==1):
        cur.execute('''DELETE FROM players_info WHERE NAME = ? ''',(name_insert,))
        conn.commit()
        print('Data deleted successfully')
        conn.close
        return 1
    else:
        print('No such file')
        conn.commit()
        conn.close
        return 0

def find_info(name_insert):
    conn=sqlite3.connect(file)
    cur = conn.cursor()
    cur.execute('''SELECT count(*) FROM players_info WHERE NAME=?''',(name_insert,))
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
        

create_file()
#insert_info(1,'Chao','calm')
#read_info()
#update_info(1,'Cool','cool')

while(1):
    selection=input('Select 1 for Insert; 2 for Read; 3 for Update; 4 for Delete; 5 for Read all\n')
    if(selection=='1'):
        ID=input('ID: ')
        Name=input('Name: ')
        Character=input('Character: ')
        other=input('Other: ')
        insert_info(ID,Name,Character,other)
    elif(selection=='2'):
        Name=input('Name: ')
        read_info(Name)
    elif(selection=='3'):
        Name=input('Name: ')
        Character=input('Character: ')
        other=input('Other: ')
        update_info(Name,Character,other)
    elif(selection=='4'):
        name=input('Name: ')
        delete_info(name)
    elif(selection=='5'):
        read_all()
    else:
        print('Try in again.')

