import tkinter
from tkinter import ttk
import time
import string
from random import randint
import user_io
import numpy

# initialization
user_io.create_file()

player_name=''
stre=''
inte=''
agi=''
defe=''
fai=''
san=''
luc=''
head=''
arm=''
weap=''
foot=''

HP_val=100

user_input='' # set a string to store user's input
entered=0 # check if user type in anything through Entry
lets_rock=0 # game start flag
speed_var=0
go_back_to_last=0
move_on=0

# sub functions
def reset_status():
    global stre,inte,agi,defe,fai,san,luc,head,arm,weap,foot
    player_name=''
    stre=''
    inte=''
    agi=''
    defe=''
    fai=''
    san=''
    luc=''
    head=''
    arm=''
    weap=''
    foot=''
    return

def random_generate_status():
    global stre,inte,agi,defe,fai,san,luc,head,arm,weap,foot
    stre=str(randint(1,15))
    inte=str(randint(1,15))
    agi=str(randint(2,15))
    defe=str(randint(3,15))
    fai=str(randint(5,15))
    san=str(randint(20,40))
    luc=str(randint(1,10))
    head='Casual Hat'
    arm='Casual Cloth'
    weap='Twig'
    foot='Casual Shoes'
    return

def get_from_array(arr):
    global player_name,stre,inte,agi,defe,fai,san,luc,head,arm,weap,foot
    player_name=arr[0]
    g_stre=arr[1]
    inte=arr[2]
    agi=arr[3]
    defe=arr[4]
    fai=arr[5]
    san=arr[6]
    luc=arr[7]
    head=arr[8]
    arm=arr[9]
    weap=arr[10]
    foot=arr[11]
    return

def Remap(Old_Min,Old_Max,New_Min,New_Max):
    # don't need it now, may be usefull in the future
    return

def cross_flie_var_trans():
    global player_name,stre,inte,agi,defe,fai,san,luc,head,arm,weap,foot
    player_name=sub_func.player_name
    stre=sub_func.stre
    inte=sub_func.inte
    agi=sub_func.agi
    defe=sub_func.defe
    fai=sub_func.fai
    san=sub_func.san
    luc=sub_func.luc
    head=sub_func.head
    arm=sub_func.arm
    weap=sub_func.weap
    foot=sub_func.foot
    return

def reduce_speed():
    ass=0
    ass=100-int(speed_val.get())
    delay(ass)
    return

def endWindow():
    script.config(state='disabled')
    window.update()
    window.destroy()
    return

def TN(Name): # Type in Name
    global entered
    PName=''
    entered=0 # with new line, the user is not entering
    type_in.config(state='disabled') # not allowed entering between lines
    enter_button.config(state='disabled')
    PName=Name+': '
    for i in range(0,len(PName)):
        script.config(state='normal')
        script.insert('end',PName[i])
        window.update()
        script.see('end') # auto scroll the scrollbar
        script.config(state='disabled')
        reduce_speed() # delay 70 ms by default
        window.update()
    delay(400)
    window.update()
    type_in.config(state='normal')
    enter_button.config(state='normal')
    return

def TL(Line): # Type in Lines
    global entered
    entered=0 # with new line, the user is not entering
    type_in.config(state='disabled') # not allowed entering between lines
    enter_button.config(state='disabled')
    for i in range(0,len(Line)):
        script.config(state='normal')
        script.insert('end',Line[i])
        window.update()
        script.see('end') # auto scroll the scrollbar
        script.config(state='disabled')
        reduce_speed() # delay 70 ms by default
        window.update()
    delay(400)
    window.update()
    type_in.config(state='normal')
    enter_button.config(state='normal')
    return

def InsDisplay(words): # Instantly display texts
    global entered
    entered=0 # with new line, the user is not entering
    type_in.config(state='disabled') # not allowed entering between lines
    enter_button.config(state='disabled')
    script.config(state='normal')
    script.insert('end',words)
    window.update()
    script.see('end') # auto scroll the scrollbar
    script.config(state='disabled')
    window.update()
    delay(400)
    window.update()
    type_in.config(state='normal')
    enter_button.config(state='normal')
    return

def GT(event=None): # Get Text
    global entered,user_input
    user_input=type_in.get()
    print('The input is '+user_input)
    entered=1
    type_in.delete(0,'end')
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
    print('Get Started')
    return

def delay(t):
    window.after(t)
    return



# ----- General Initialization ----- #
window = tkinter.Tk()
window.title('Take A New Adventure')
window.geometry('810x500') # 0.618 ratio
window.resizable(width=False, height=False)
window.configure(background='cornflower blue')

# ----- Scrollbar Initialization ----- #
bar = tkinter.Scrollbar(window)
bar.pack(side='right',fill='y')

# ----- Text Initialization ----- #
script = tkinter.Text(window,font=('Aerial',18),yscrollcommand=bar.set)
script.pack(side='left',fill='x')
script.place(anchor='nw',x=10,y=10,height=320,width=540)
script.configure(padx=10,pady=10,wrap='word',spacing1=5,spacing2=4,spacing3=5,
background='LightCyan2')

# ----- Entry Initialization ----- #
type_in = tkinter.Entry(window,font=(18))
type_in.bind('<Return>',GT) # GT=Get Lines
type_in.pack()
type_in.place(anchor='nw',x=10,y=345,width=150)

# ----- Start Game Button Initialization ----- #
start_button = tkinter.Button(window,text='Start Game',font=(14),command=Start)
start_button.pack()
start_button.place(anchor='nw',x=10,y=385,height=30,width=90)

# ----- Exit Button Initialization ----- #
exit_button = tkinter.Button(window,text='Exit',font=(14),command=endWindow)
exit_button.pack()
exit_button.place(anchor='nw',x=110,y=385,height=30,width=60)

# ----- Enter Button Initialization ----- #
enter_button = tkinter.Button(window,text='Enter',font=(14),command=GT)
enter_button.pack()
enter_button.place(anchor='nw',x=170,y=345,height=30,width=60)

# ----- Speed Bar Initialization ----- #
speed_val = tkinter.IntVar()
speed_bar = tkinter.Scale(window,variable = speed_val,
orient='horizontal',label='Game Speed+ Control Bar')
speed_bar.pack()
speed_bar.place(anchor='nw',x=560,y=345,width=224,height=60)
speed_bar.configure(background='LightCyan2',activebackground='cyan3')

# ----- HP Frame contains Process Bar & Label ----- #
theme_setting = ttk.Style()
theme_setting.theme_use('classic') #('aqua', 'clam', 'alt', 'default', 'classic') are the choices
theme_setting.configure("HP.Horizontal.TProgressbar", troughcolor='SteelBlue1', background='pale green')

HP_frame = tkinter.Frame(window,background='LightCyan2')
HP_frame.pack()
HP_frame.place(anchor='ne',x=550,y=345,width=160,height=60)

HP_label1 = tkinter.Label(HP_frame,text='HP',bd=4,background='LightCyan2')
HP_label1.pack()
HP_label1.place(anchor='nw',x=0,y=0)

HP_bar = ttk.Progressbar(HP_frame,orient='horizontal',length=150,mode='determinate')
HP_bar.pack()
HP_bar.config(value=HP_val,style='HP.Horizontal.TProgressbar')
HP_bar.place(anchor='n',x=80,y=30)

HP_val_label = tkinter.Label(HP_frame,bd=4,background='LightCyan2')
HP_val_label.pack()
HP_val_label.configure(text=str(HP_val)+'/100')
HP_val_label.place(anchor='ne',x=160,y=0)

# ----- Player Status Info Frame ----- #
player_info_frame = tkinter.Frame(window,relief='groove')
player_info_frame.pack()
player_info_frame.place(anchor='nw',x=560,y=10,height=190,width=224)
player_info_frame.configure(background='LightCyan2')

player_info_name = tkinter.Label(player_info_frame,text="Your Name",background='LightCyan2')
player_info_name.pack()
player_info_name.place(anchor='n',x=112,y=10)

player_info_name2 = tkinter.Label(player_info_frame,background='LightCyan2')
player_info_name2.pack()
player_info_name2.place(anchor='n',x=112,y=30)

player_status_frame = tkinter.Frame(player_info_frame,background='LightCyan2')
player_status_frame.pack()
player_status_frame.place(anchor='n',x=112,y=55,height=125,width=170)

player_status_name = tkinter.Listbox(player_status_frame,bd=0,background='LightCyan2')
player_status_name.pack()
player_status_name.place(anchor='nw',x=0,y=0,height=125,width=65)
player_status_name.insert(1,'Strenth ')
player_status_name.insert(2,'Intellect ')
player_status_name.insert(3,'Agility ')
player_status_name.insert(4,'Defense ')
player_status_name.insert(5,'Faith ')
player_status_name.insert(6,'Sanity ')
player_status_name.insert(7,'Luck ')
player_status_name.config(justify='right')

player_status_val = tkinter.Listbox(player_status_frame,bd=0,background='LightCyan2')
player_status_val.pack()
player_status_val.place(anchor='n',x=100,y=0,height=125,width=40)
player_status_val.config(justify='center')
for i in range(0,7):
    player_status_val.insert(i,'0')

player_status_addval = tkinter.Listbox(player_status_frame,bd=0,background='LightCyan2')
player_status_addval.pack()
player_status_addval.place(anchor='ne',x=160,y=0,height=125,width=40)
player_status_addval.config(justify='center')
for i in range(0,7):
    player_status_addval.insert(i,'+0')

# ----- Player Wear Info Frame ----- #
player_wear_frame = tkinter.Frame(window,relief='groove')
player_wear_frame.pack()
player_wear_frame.place(anchor='nw',x=560,y=210,height=120,width=224)
player_wear_frame.configure(background='LightCyan2')

player_wear_frame_name = tkinter.Label(player_wear_frame,text="Equipment",background='LightCyan2')
player_wear_frame_name.pack()
player_wear_frame_name.place(anchor='n',x=112,y=5)

player_headwear = tkinter.Label(player_wear_frame,text="Headwear",background='LightCyan2')
player_headwear.pack()
player_headwear.place(anchor='n',x=50,y=30)

player_headwear2 = tkinter.Label(player_wear_frame,background='LightCyan2',text='None')
player_headwear2.pack()
player_headwear2.place(anchor='n',x=50,y=50)

player_armour = tkinter.Label(player_wear_frame,text="Armour",background='LightCyan2')
player_armour.pack()
player_armour.place(anchor='n',x=174,y=30)

player_armour2 = tkinter.Label(player_wear_frame,background='LightCyan2',text='None')
player_armour2.pack()
player_armour2.place(anchor='n',x=174,y=50)

player_weapon = tkinter.Label(player_wear_frame,text="Weapon",background='LightCyan2')
player_weapon.pack()
player_weapon.place(anchor='n',x=50,y=70)

player_weapon2 = tkinter.Label(player_wear_frame,background='LightCyan2',text='None')
player_weapon2.pack()
player_weapon2.place(anchor='n',x=50,y=90)

player_footwear = tkinter.Label(player_wear_frame,text="Footwear",background='LightCyan2')
player_footwear.pack()
player_footwear.place(anchor='n',x=174,y=70)

player_footwear2 = tkinter.Label(player_wear_frame,background='LightCyan2',text='None')
player_footwear2.pack()
player_footwear2.place(anchor='n',x=174,y=90)

# ---- <Update Status Showing> ---- #
def update_status_showing():
    player_info_name2.config(text=player_name)
    formed=[stre,inte,agi,defe,fai,san,luc]
    player_status_val.delete(0,'end') # clear listbox
    for j in range(0,7):
        player_status_val.insert(j+1,formed[j])
    player_headwear2.config(text=head)
    player_armour2.config(text=arm)
    player_weapon2.config(text=weap)
    player_footwear2.config(text=foot)
    return

# ---- <Branch Scripts> ---- #
def beginning_script():
    global user_input,entered,move_on
    TL('Hello, there, welcome to our game.\n')
    TL('What would you like to do?\n')
    InsDisplay('1.Start as a new player\n2.Load from saved player\n\n')

    while(1):
        wait_for_input()
        if(user_input!=''):
            if(user_input=='1'):
                move_on=1
                break
            elif(user_input=='2'):
                move_on=2
                break
            else:
                entered==0
                InsDisplay('Please enter at least 1 word.\n')
    user_input=''
    return


def newgame_script():
    global user_input,player_name,entered
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
                if(user_io.find_info(user_input)==1):
                    InsDisplay('This name exists, please try another one.\n')
                else:
                    InsDisplay('Now generating your status.')
                    TL('.....\n')
                    random_generate_status()
                    cross_flie_var_trans()
                    player_name=user_input
                    user_io.insert_info(player_name,stre,inte,agi,defe,fai,
                                        san,luc,head,arm,weap,foot)
                    update_status_showing()
                    InsDisplay('Done\n')
                    break
            else:
                InsDisplay('Please enter less than 6 words.\n')
        else:
            entered==0
            InsDisplay('Please enter at least 1 word.\n')
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
                TN('Lu')
                TL('Wonderful! Now the first task is to explore the village outside of the town.\n')
                TN('Lu')
                TL('Once you get there, you will know what to do.\n')
                break
            elif(user_input=='2'):
                TN(player_name)
                TL('Nope, not really.\n')
                TN('Lu')
                TL('Sure thing, my friend. See you in a little bit.\n')
                break
            else:
                entered==0
                InsDisplay('Please enter 1 or 2.\n')
        else:
            InsDisplay('Please enter at least 1 word.\n')
    user_input=''
    return

def saved_review():
    global user_input,entered,move_on,go_back_to_last
    go_back_to_last=0
    move_on=0
    while(1):
        TL('Please select:\n')
        InsDisplay('1.Review all saved player files.\n')
        InsDisplay('2.Load one file.\n')
        InsDisplay('3.Delete one file.\n')
        InsDisplay('4.Return to main meau.\n')
        wait_for_input()
        if(user_input!=''):
            if(user_input=='1'):
                ass = user_io.read_all()
                if(user_io.empty_check()==1):
                    InsDisplay('\nDisplaying...\n')
                    InsDisplay('Please select one name to display detail.\n')
                    for j in range (0,len(ass)):
                        InsDisplay(' '+ass[j][0]+'\n')
                    user_input=''
                    wait_for_input()
                    while(1):
                        if(user_input!=''):
                            if(user_io.find_info(user_input)==1):
                                InsDisplay('Please see status list for details\n\n')
                                ass2 = user_io.read_info(user_input)
                                get_from_array(ass2)
                                cross_flie_var_trans()
                                update_status_showing()
                                break
                            else:
                                InsDisplay('No such name.\n\n')
                                break
                        else:
                            InsDisplay('Please enter at least 1 word.\n')
                    user_input=''
                else:
                    TL('\nNo data in database.\n\n')
            elif(user_input=='2'):
                InsDisplay('\nPlease type in the name.\n')
                wait_for_input()
                while(1):
                    if(user_input!=''):
                        if(user_io.find_info(user_input)==0):
                            InsDisplay('No such name.\n\n')
                            break
                        else:
                            TL('Loading...\n')
                            ass2 = user_io.read_info(user_input)
                            get_from_array(ass2)
                            cross_flie_var_trans()
                            update_status_showing()
                            InsDisplay('Done!\n')
                            TL('Welcome back, '+player_name+'.\n\n')
                            move_on=1
                            go_back_to_last=1
                            break
                    else:
                        InsDisplay('Please enter at least 1 word.\n')
                user_input=''
            elif(user_input=='3'):
                InsDisplay('\nPlease type in the name to delete.\n')
                wait_for_input()
                while(1):
                    if(user_input!=''):
                        if(user_io.find_info(user_input)==0):
                            InsDisplay('No such name.\n\n')
                            break
                        else:
                            TL('Deleting...\n')
                            user_io.delete_info(user_input)
                            reset_status()
                            cross_flie_var_trans()
                            update_status_showing()
                            InsDisplay('Done!\n\n')
                            move_on=0
                            break
                    else:
                        InsDisplay('Please enter at least 1 word.\n')
                user_input=''
            elif(user_input=='4'):
                go_back_to_last=1
            else:
                entered=0
                go_back_to_last=0
                TL('Please enter 1, 2, 3, or 4.\n\n')
        else:
            InsDisplay('Please enter at least 1 word.\n')
            
        if(move_on==1):
            move_on=0
            break
        if(go_back_to_last==1):
            go_back_to_last=0
            InsDisplay('\n')
            break
    user_input=''
    return

# ---- <Main Script> ---- #

def demo_HP_bar():
    for i in range(0,101):
        HP_val=i
        HP_bar.config(value=HP_val)
        HP_val_label.configure(text=str(HP_val)+'/100')
        window.update()
        delay(50)
    delay(200)
    for i in range(0,101):
        HP_val=100-i
        HP_bar.config(value=HP_val)
        HP_val_label.configure(text=str(HP_val)+'/100')
        window.update()
        delay(50)
    return

InsDisplay('Demo - HP bar rolling, game will be starting soon. \n\n')

demo_HP_bar()


while(lets_rock==0):
    window.update()
    print('Press Start Game to begin.')
lets_rock==0

while(go_back_to_last==0):
    beginning_script()
    if(move_on==1):
        newgame_script()
        break
    else:
        saved_review()

TN('Lu')
TL('Let the adventure begin!\n')


TL('\n\nTo be continued...\n')
window.mainloop()
