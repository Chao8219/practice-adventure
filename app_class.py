import tkinter as tk

class Application(tk.Frame):
    """ This class is to create a tkinter application instance
    
    Please use method down below to create the application
    import app_class
    import tkinter as tk
    root = tk.Tk()
    app = app_class.Application(master=root)
    app.mainloop()
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(anchor='w', fill='both', expand='1') 
        self.create_widgets()
    
    def create_widgets(self):
        self.create_scroll_bar()
        self.create_script()

    def create_scroll_bar(self):
        self.bar = tk.Scrollbar(self)
        self.bar.pack(side='right',fill='y')

    def create_script(self):
        self.script = tk.Text(self, font=('Aerial',18), 
                            yscrollcommand=self.bar.set)
        self.script.pack(side='left', fill='x')
        self.script.place(anchor='nw', x=10, y=10, height=320, width=540)
        self.script.configure(padx=10, pady=10, wrap='word', spacing1=5, 
                            spacing2=4, spacing3=5, 
                            background='LightCyan2')

if __name__ == '__main__':
    print('Please import this module to create the application.')