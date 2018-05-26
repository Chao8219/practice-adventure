from tkinter import *
import time
import string
import pickle

user_input='' # set a string to store user's input
entered=0 # check if user type in anything through Entry
lets_rock=0 # game start flag
speed_var=0
player_name=''

def reduce_speed():
    ass=0
    ass=70-int(speed_val.get()/1.45)
    delay(ass)
    return
    
def Remap(Old_Min,Old_Max,New_Min,New_Max):
    # don't need it now, may be usefull in the future
    return

def endWindow():
    script.config(state=DISABLED)
    window.update()
    window.destroy()
    return

def TN(Name): # Type in Name
    global entered
    PName=''
    entered=0 # with new line, the user is not entering
    type_in.config(state=DISABLED) # not allowed entering between lines
    enter_button.config(state=DISABLED)
    PName=Name+': '
    for i in range(0,len(PName)):
        script.config(state=NORMAL)
        script.insert(END,PName[i])
        window.update()
        script.see(END) # auto scroll the scrollbar
        script.config(state=DISABLED)
        reduce_speed() # delay 70 ms by default
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
        reduce_speed() # delay 70 ms by default
        window.update()
    delay(400)
    window.update()
    type_in.config(state=NORMAL)
    enter_button.config(state=NORMAL)
    return

def InsDisplay(words): # Instantly display texts
    global entered
    entered=0 # with new line, the user is not entering
    type_in.config(state=DISABLED) # not allowed entering between lines
    enter_button.config(state=DISABLED)
    script.config(state=NORMAL)
    script.insert(END,words)
    window.update()
    script.see(END) # auto scroll the scrollbar
    script.config(state=DISABLED)
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

# ----- General Initialization ----- #
window=Tk()
window.title('Take An New Adventure')
window.geometry('810x500') # 0.618 ratio
window.resizable(width=False, height=False)
window.configure(background='cornflower blue')

# ----- Scrollbar Initialization ----- #
bar=Scrollbar(window)
bar.pack(side=RIGHT,fill=Y)

# ----- Text Initialization ----- #
script=Text(window,font=('Aerial',18),yscrollcommand=bar.set)
script.pack(side=LEFT,fill=X)
script.place(anchor=NW,x=10,y=10,height=320,width=540)
script.configure(padx=10,pady=10,wrap=WORD,spacing1=5,spacing2=4,spacing3=5,background='LightCyan2')

# ----- Entry Initialization ----- #
type_in=Entry(window,font=(18))
type_in.bind('<Return>',GT) # GT=Get Lines
type_in.pack()
type_in.place(anchor=NW,x=10,y=345,width=150)

# ----- Start Game Button Initialization ----- #
start_button=Button(window,text='Start Game',font=(14),command=Start)
start_button.pack()
start_button.place(anchor=NW,x=10,y=385,height=30,width=90)

# ----- Exit Button Initialization ----- #
exit_button=Button(window,text='Exit',font=(14),command=endWindow)
exit_button.pack()
exit_button.place(anchor=NW,x=110,y=385,height=30,width=60)

# ----- Enter Button Initialization ----- #
enter_button=Button(window,text='Enter',font=(14),command=GT)
enter_button.pack()
enter_button.place(anchor=NW,x=170,y=345,height=30,width=60)

# ----- Speed Bar Initialization ----- #
speed_val = IntVar()
speed_bar=Scale(window,variable = speed_val,orient=HORIZONTAL,label='Game Speed+ Control Bar')
speed_bar.pack()
speed_bar.config()
speed_bar.place(anchor=NW,x=560,y=345,width=224)
speed_bar.configure(background='LightCyan2',activebackground='cyan3')

# ----- Player Info Frame ----- #
player_info_frame=Frame(window,relief=GROOVE)
player_info_frame.pack()
player_info_frame.place(anchor=NW,x=560,y=10,height=320,width=224)
player_info_frame.configure(background='LightCyan2')

player_info_name=Label(player_info_frame,text="Your Name",background='LightCyan2')
player_info_name.pack()
player_info_name.place(anchor=N,x=112,y=10)

player_info_name2=Label(player_info_frame,background='LightCyan2')
player_info_name2.pack()
player_info_name2.place(anchor=N,x=112,y=30)

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

# ---- <Test Texts 2> ---- #
##TN('Axx')
##TL('中文字体\n')
##TN('ABCde')
##TL('这是一大长串的字符，要换行的那种，看看效果怎么样。估计字符数量可能需要很多才能换行\n')
##TN('ABCDE')
##TL('mmmmmmmmm ssssssss wwwwww rrrrrrr qqqqq zzzzz ttttt sssss cccccc\n')
# ---- </Test Texts 2> ---- #

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
lets_rock==0

TN('???')
TL('Greating, my friend!\n')
delay(300)
TN('???')
TL('Welcome to Baguette\'s World!\n')
delay(300)
TN('???')
TL('Dear adventurer,')
delay(100)
TL(' may I have your name?\n')
InsDisplay('Your name:\n')
while(1):
    wait_for_input()
    if(user_input!=''):
        if(len(user_input)<=6):
            player_name=user_input
            player_info_name2.config(text=player_name)
            break
        else:
            TL('Please enter less than 6 words.\n')
    else:
        entered==0
        TL('Please enter at least 1 word.\n')
user_input=''        
TN(player_name)
TL('Hi, I am '+player_name+'.\n')

if(player_name=='Lucas' or player_name=='lucas'):
    TN('???')
    TL('Hmm, my name is Lucas as well, Lucas Murphy. ')
    delay(100)
    TL('You can call me Lu.\n')
elif(player_name=='Lu' or player_name=='lu'):
    TN('???')
    TL('Hmm, my name is Lu as well, Lucas Murphy. ')
    delay(100)
    TL('You can call me Lu too.\n')
else:
    TN('???')
    TL('Hello, '+player_name+', it is a great honor to meet you.\n')
    TN('???')
    TL('My name is Lucas Murphy. You can call me Lu.\n')

TN('Lu')
TL('Dear adventurer,')
delay(300)
TL(' you may wonder why you are here. Please allow me to ellaborate it for you.\n')
delay(300)
TN('Lu')
TL(player_name+', '+'you are summoned to this world by our greatest wizard \"Alexandra Lyapunov\" who once defeated the Evil Slime King.\n')
TN('Lu')
TL('The reason why he summons you is that, he sees the potential on you.\n')
TN('Lu')
TL('He believes, provided by opportunity, you will become one of the best warriors in this world.\n')
TN('Lu')
TL(player_name+', '+'would you like to accpet your first mission to begin your journey?\n')
InsDisplay('Your choice: \n')
InsDisplay(' 1.Yes\n 2.No\n')

while(1):
    wait_for_input()
    if(user_input!=''):
        if(user_input=='1'):
            TN(player_name)
            TL('I very much do.\n')
            break
        elif(user_input=='2'):
            TN(player_name)
            TL('Nope, not really.\n')
            TN('Lu')
            TL('Sure thing, my friend. See you in a little bit.\n')
            InsDisplay('Game\'s over, please restart game.\n')
            break
        else:
            entered==0
            TL('Please enter 1 or 2.\n')
    else:
        TL('Please enter at least 1 word.\n')
user_input=''



TL('\n\nTo be continued...\n')


window.mainloop()
