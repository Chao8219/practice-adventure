from tkinter import *
import time

user_sub='' # set a string to store user's input
entered=0 # check if user type in anything through Entry

def endWindow():
    window.quit()
    window.destroy()
    return

def TypeLine(Line):
    global entered
    entered=0 # with new line, the user is not entering
    type_in.config(state='disabled') # not allowed entering between lines
    size=len(Line)
    for i in range(0,size):
        script.config(state='normal')
        script.insert('end',Line[i])
        script.see('end') # auto scroll the scrollbar
        script.config(state='disabled')
        window.update()
        window.after(100) # delay 100 ms
    window.after(400)
    window.update()
    type_in.config(state='normal')
    return

def getText(event=None):
    global entered,user_sub
    user_sub=type_in.get()
    print('The input is '+user_sub)
    entered=1
    type_in.delete(0,'end')
    window.update()
    return

def wait_for_input():
    while(entered==0):
        print('waiting...')
        window.update()
    return

# ---- General Initialization ---- #
window=Tk()
window.title('Pre_GUI')
window.geometry('600x500')
window.resizable(width=False, height=False)

# ----- Scrollbar Initialization ---- #
bar=Scrollbar(window)
bar.pack(side='right',fill='y')

# ----- Text Initialization ---- #
script=Text(window,relief=RIDGE,font=("Helvetica",20),yscrollcommand=bar.set)
script.pack(side='left',fill='x')
script.place(anchor='n',x=300,y=20,height=400,width=500)

# ----- Button Initialization ---- #
exit_button=Button(window,text='Exit',command=endWindow)
exit_button.pack()
exit_button.place(anchor=S,x=300,y=490,height=40,width=50)

# ----- Entry Initialization ---- #
type_in=Entry(window)
type_in.bind('<Return>',getText)
type_in.pack()
type_in.place(anchor=S,x=300,y=450,width=200)

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
while(1):
    Line1='Who are you?\n'
    TypeLine(Line1)
    wait_for_input()
    if(user_sub=='Jack' or user_sub=='jack'):
        TypeLine('Jack, welcome back.\n')
        break
    elif(user_sub!=''):
        TypeLine('Are you sure, Jack?\n')
    else:
        TypeLine('Please type anything.\n')

TypeLine('I am your host, Alex.\n')
# ---- </Test Texts with input> ---- #

window.mainloop()
