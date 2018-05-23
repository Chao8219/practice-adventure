from tkinter import *
import time

def endWindow():
    window.destroy()
    return

def TypeInLine(Line):
    size=len(Line)
    for i in range(0,size):
        script.config(state=NORMAL)
        script.insert(END,Line[i])
        script.see(END) # auto scroll the scrollbar
        script.config(state=DISABLED)
        window.update()
        time.sleep(0.1)
    return

def getText():
    print('Anything')
    return

# ---- General Initialization ---- #
window=Tk()
window.title('Pre_GUI')
window.geometry('600x500')
window.resizable(width=False, height=False)

# ----- Scrollbar Initialization ---- #
bar=Scrollbar(window)
bar.pack(side=RIGHT,fill=Y)

# ----- Text Initialization ---- #
script=Text(window,relief=RIDGE,font=("Helvetica",20),yscrollcommand=bar.set)
script.pack(side=LEFT,fill=X)
script.place(anchor=N,x=300,y=20,height=400,width=500)

# ----- Button Initialization ---- #
exit_button=Button(window,text='Exit',command=endWindow)
exit_button.pack()
exit_button.place(anchor=S,x=300,y=490,height=40,width=50)

# ----- Entry Initialization ---- #
type_in=Entry(window)
type_in.pack()
type_in.place(anchor=S,x=300,y=450,width=200)

Line_test='Welcome to the GUI debug world.\n'
TypeInLine(Line_test)
Line_test2='I am your host, Will.\n'
TypeInLine(Line_test2)
Line_test3='Many bugs may appear in this world, such as xhckjendksdjck and u4iwksjdcuhe2uo3432\n'
TypeInLine(Line_test3)
Line_test4='But,\n'+'so far\n'+'so good.\n'
TypeInLine(Line_test4)
Line_test5='I wonder\n'+'if\n'+'we\n'+'simply\n'+'create\n'+'many\n'+'lines\n'+'Then\n'+'what\n'+'would\n'+'happen?\n'
TypeInLine(Line_test5)

window.mainloop()
