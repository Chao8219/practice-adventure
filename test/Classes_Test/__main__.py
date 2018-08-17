import tkinter as tk

class MainApp(tk.Frame):
    def __init__(self,parent,*args,**kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)
        self.parent=parent

if __name__=="__main__":
    root=tk.Tk()
    root.title('Here is a title.')
    root.geometry('810x500') # 0.618 ratio
    root.resizable(width=False, height=False)
    MainApp(root).pack(side='top',fill='both',expand=True)
    root.mainloop
