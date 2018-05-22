import string
import random
import time
import os

def WordbyWord(Line):
    size=len(Line)
    i=0;
    while(i<size):
        print(Line[i],end='')
        i=i+1
        time.sleep(0.1)
    print('')
    time.sleep(1)
    return
def TypeName(Line):
    size=len(Line)
    i=0;
    while(i<size):
        print(Line[i],end='')
        i=i+1
        time.sleep(0.1)
    time.sleep(1)
    return

os.system('cls')  # For Windows
os.system('clear')  # For Linux/OS X

time.sleep(1)
Line0='Hello!'
WordbyWord(Line0)
Line1='Welcome to Badass\' World!'
WordbyWord(Line1)
Line2='Dear Adventurer, may I have your name?'
WordbyWord(Line2)
player_name=input('Your name: ')
time.sleep(0.5)
Line3_1='Great! '
TypeName(Line3_1)
Line3_2=player_name+', '
TypeName(Line3_2)
if(player_name=='Jack' or player_name=='jack'):
    Line3_3_1_1="My name is Jack too, "
    TypeName(Line3_3_1_1)
    Line3_3_1_2="shall I introduce the background to you?"
    WordbyWord(Line3_3_2)
else:
    Line3_3_2_1="My name is Jack Murphy, "
    TypeName(Line3_3_2_1)
    Line3_3_2_2="shall I introduce the background to you?"
    WordbyWord(Line3_3_2_2)
print('1.Yes')
print('2.No')
print('3.Go away, just leave me alone')
while(1):
    selection1=input('Your choice: ')
    if(selection1=='1'):
        Line4='The Background is...'
        WordbyWord(Line4)
        break
    elif(selection1=='2'):
        Line5='Fine, if you insist.'
        WordbyWord(Line5)
        break
    elif(selection1=='3'):
        Line6='Sure thing, my friend.'
        WordbyWord(Line6)
        break
    else:
        Line7_1=player_name+', '
        TypeName(Line7_1)
        Line7_2='Please re-choose your choice'
        WordbyWord(Line7_2)

