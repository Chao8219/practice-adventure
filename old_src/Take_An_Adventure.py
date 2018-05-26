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
    Line3_3_1_1="my name is Jack too, "
    TypeName(Line3_3_1_1)
    Line3_3_1_2="shall I introduce the background to you?"
    WordbyWord(Line3_3_2)
else:
    Line3_3_2_1="my name is Jack Murphy, "
    TypeName(Line3_3_2_1)
    Line3_3_2_2="shall I introduce the background to you?"
    WordbyWord(Line3_3_2_2)
print('1.Yes')
print('2.No')
print('3.Go away, just leave me alone')
while(1):
    selection1=input('Your choice: ')
    if(selection1=='1'):
        Line4_name=player_name+', ';
        TypeName(Line4_name)
        Line4='you may wonder why you are here.'
        WordbyWord(Line4)
        Line4_2='The truth is,'
        TypeName(Line4_2)
        Line4_3=' you were summoned to this world by the greatest wizard \"Alexandra Lyapunov\" who once defeated the Evil Slime King.'
        WordbyWord(Line4_3)
        Line4_4='However,the frustraing truth is that, '
        TypeName(Line4_4)
        Line4_5='every time you killed him, the Evil Slime King would be stronger.'
        WordbyWord(Line4_5)
        Line4_6='My friend, you know what a slime looks like, right?'
        WordbyWord(Line4_6)
        Line4_7='A slime has no solid body, no certain form. '
        TypeName(Line4_7)
        Line4_8='They can be whatever they want to be.'
        WordbyWord(Line4_8)
        Line4_9='The last Evil Slime King became a gaint chocolate pudding which was almost the most delicious food in this world.'
        WordbyWord(Line4_9)
        Line4_10='No ordinary man could resist it. They all wanted to take a bite.'
        WordbyWord(Line4_10)
        Line4_11='The gaint pudding was so gaint that the human being could never consume it all.'
        WordbyWord(Line4_11)
        Line4_12='Our greatest wizard couldn\'t bear to see all humankind suffered from the fat which was brought by immoderately eatting the pudding. '
        WordbyWord(Line4_12)
        Line4_13='He went to challenge the Evil Slime King.'
        WordbyWord(Line4_13)
        Line4_14='Of course, he won the battle. But the price he paid was way to huge.'
        TypeName(Line4_14)
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        Line4_15='Now, he\'s dying from severe diabetes.'
        WordbyWord(Line4_15)
        Line4_16='He wants you to be the warrior to save people from the next Evil Slime King.'
        WordbyWord(Line4_16)
        Line4_17='Sorry to keep you hearing all the story. Now it is time to go on an adventure!'
        WordbyWord(Line4_17)
        break
    elif(selection1=='2'):
        Line5='Fine, if you insist.'
        WordbyWord(Line5)
        Line5_2='Let\'s go on an advanture then!'
        WordbyWord(Line5_2)
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

