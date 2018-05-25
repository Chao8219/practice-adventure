from tkinter import *
import time

user_input='' # set a string to store user's input
entered=0 # check if user type in anything through Entry
lets_rock=0 # game start flag

player_name=''

def endWindow():
    script.config(state=DISABLED)
    window.update()
    window.destroy()
    return

def TN(Name): # Type in Name
    global entered
    entered=0 # with new line, the user is not entering
    type_in.config(state=DISABLED) # not allowed entering between lines
    enter_button.config(state=DISABLED)
    for i in range(0,len(Name)):
        script.config(state=NORMAL)
        script.insert(END,Name[i])
        window.update()
        script.see(END) # auto scroll the scrollbar
        script.config(state=DISABLED)
        delay(100) # delay 100 ms
        window.update()
    delay(400)
    window.update()
    type_in.config(state=NORMAL)
    enter_button.config(state=NORMAL)
    return

def TL(Line): # Type in Lines
    global entered
    entered=0 # with new line, the user is not entering
    type_in.config(state=DISABLED) # not allowed entering between lines
    enter_button.config(state=DISABLED)
    for i in range(0,len(Line)):
        script.config(state=NORMAL)
        script.insert(END,Line[i])
        window.update()
        script.see(END) # auto scroll the scrollbar
        script.config(state=DISABLED)
        delay(100) # delay 100 ms
        window.update()
    delay(400)
    window.update()
    type_in.config(state=NORMAL)
    enter_button.config(state=NORMAL)
    return

def GT(event=None): # Get Text
    global entered,user_input
    user_input=type_in.get()
    print('The input is '+user_input)
    entered=1
    type_in.delete(0,END)
    window.update()
    return

def wait_for_input():
    while(entered==0):
        print('waiting... please input data.')
        window.update()
    return

def Start(event=None):
    global lets_rock
    lets_rock=1
    return

def delay(t):
    window.after(t)
    return

# ---- General Initialization ---- #
window=Tk()
window.title('Take An New Adventure')
window.geometry('650x400') # 0.618 ratio
window.resizable(width=False, height=False)
window.configure(background='cornflower blue')

# ----- Scrollbar Initialization ---- #
bar=Scrollbar(window)
bar.pack(side=RIGHT,fill=Y)

# ----- Text Initialization ---- #
script=Text(window,font=("Helvetica",18),yscrollcommand=bar.set)
script.pack(side=LEFT,fill=X)
script.place(anchor=NW,x=10,y=10,height=320,width=540)
script.configure(wrap=WORD,spacing1=4,spacing2=4,spacing3=4,background='LightCyan2')

# ----- Entry Initialization ---- #
type_in=Entry(window,font=("Helvetica",18))
type_in.bind('<Return>',GT) # GT=Get Lines
type_in.pack()
type_in.place(anchor=NW,x=10,y=345,width=150)

# ----- Start Game Button Initialization ---- #
start_button=Button(window,text='Start Game',font=("Helvetica",14),command=Start)
start_button.pack()
start_button.place(anchor=NW,x=240,y=345,height=30,width=90)

# ----- Enter Button Initialization ---- #
enter_button=Button(window,text='Enter',font=("Helvetica",14),command=GT)
enter_button.pack()
enter_button.place(anchor=NW,x=170,y=345,height=30,width=60)

# ----- Exit Button Initialization ---- #
exit_button=Button(window,text='Exit',font=("Helvetica",14),command=endWindow)
exit_button.pack()
exit_button.place(anchor=NE,x=620,y=345,height=30,width=60)

# ---- <Test Texts> ---- #
##Line_test='Welcome to the GUI debug world.\n'
##TypeInLine(Line_test)
##Line_test2='I am your host, Will.\n'
##TypeInLine(Line_test2)
##Line_test3='Many bugs may appear in this world, such as xhckjendksdjck and u4iwksjdcuhe2uo3432\n'
##TypeInLine(Line_test3)
##Line_test4='But,\n'+'so far\n'+'so good.\n'
##TypeInLine(Line_test4)
##Line_test5='I wonder\n'+'if\n'+'we\n'+'simply\n'+'create\n'+'many\n'+'lines\n'+'Then\n'+'what\n'+'would\n'+'happen?\n'
##TypeInLine(Line_test5)
# ---- </Test Texts> ---- #

# ---- <Test Texts with input> ---- #
##while(1):
##    Line1='Who are you?\n'
##    TL(Line1)
##    wait_for_input()
##    if(user_input=='Jack' or user_input=='jack'):
##        TL('Jack, welcome back.\n')
##        break
##    elif(user_input!=''):
##        TL('Are you sure, Jack?\n')
##    else:
##        TL('Please type anything.\n')
##
##TL('I am your host, Alex.\n')
# ---- </Test Texts with input> ---- #

# ---- <Main> ---- #

while(lets_rock==0):
    window.update()
    print('Press Start Game to begin.')

TN('???: ')
TL('Greating, my friend!\n')
delay(300)
TN('???: ')
TL('Welcome to Baguette\'s World!\n')
delay(300)
TN('???: ')
TL('Dear Adventurer,')
TL(' may I have your name?\n')
TL('Your name:\n')
while(1):
    wait_for_input()
    if(user_input!=''):
        if(len(user_input)<=5):
            player_name=user_input
            break
        else:
            TL('Please enter less than 5 words.\n')
        
TN(player_name+': ')
TL('Hi, I am '+player_name+'.\n')
TN('???: ')
TL('Hello, '+player_name+', it is a great honor to meet you.\n')
TN('???: ')
TL('My name is Lucas Murphy. You can call me Lu.\n')
TN('Lu: ')
TL('Dear Adventurer,')
delay(300)
TL(' you may wonder why you are here. Please allow me to ellaborate it.\n')
TL('To be continued...\n')
    
window.mainloop()
