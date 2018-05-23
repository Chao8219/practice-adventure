from tkinter import *
def endWindow():
    window.destroy()

window=Tk()
window.title('Pre_GUI')
window.geometry('600x600')
bar=Scrollbar(window)
bar.pack(side=RIGHT,fill=Y)
script=Listbox(window,yscrollcommand=bar.set)
script.pack(side=LEFT,fill=X)
script.place(anchor=N,x=300,y=20,height=500,width=500)

exit_button=Button(window,text='Exit',command=endWindow)
exit_button.pack()
exit_button.place(anchor=S,x=300,y=580,height=50,width=50)

for i in range(50):
    script.insert(END,i)

window.mainloop()
