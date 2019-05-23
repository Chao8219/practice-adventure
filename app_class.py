import tkinter as tk

class Application(tk.Frame):
    """ This class is to create a tkinter application instance
    
    Please use method down below to create the application:
    --------------------------------------------
    import app_class
    import tkinter as tk
    root = tk.Tk()
    root.title('Take A New Adventure')
    root.geometry('810x500') # 0.618 ratio
    root.resizable(width=False, height=False)
    root.configure(background='cornflower blue')
    app = app_class.Application(master=root)
    app.mainloop()
    --------------------------------------------

    Attributes:
    orwell: string
        short for BIG BROTHER IS WATCHING YOU, which is a dummy name for 
        debug and test only.
    """
    orwell = 'BIG BROTHER IS WATCHING YOU'
    game_start_signal = False

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(anchor='w', fill='both', expand='1') 
        self.create_widgets()
    
    def create_widgets(self):
        self.create_scroll_bar()
        self.create_script()
        self.create_type_in()
        self.create_start_button()
        self.create_exit_button()
        self.create_enter_button()
        self.create_speed_bar()

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
    
    def create_type_in(self):
        """ Create a type-in text frame. """
        self.type_in = tk.Entry(self, font=(18))
        self.type_in.bind('<Return>', self.get_text)
        self.type_in.pack()
        self.type_in.place(anchor='nw', x=10, y=345, width=150)
    
    def create_start_button(self):
        """ Create a button to be used to start the game. """
        # somehow the font size in Windows is not showing correctly.
        self.start_button = tk.Button(self, text='Start Game', font=(14), 
                                    command=self.start_game)
        self.start_button.pack()
        self.start_button.place(anchor='nw', x=10, y=385, height=30, 
                            width=90)
    
    def create_exit_button(self):
        exit_button = tk.Button(self, text='Exit', font=(14),
                            command=self.close_window)
        exit_button.pack()
        exit_button.place(anchor='nw', x=110, y=385, height=30, width=60)

    def create_enter_button(self):
        """ Create a enter button to give users a alternative to submit
        what they have entered in the Entry widget. """
        self.enter_button = tk.Button(self, text='Enter', font=(14), 
                                    command=self.get_text)
        self.enter_button.pack()
        self.enter_button.place(anchor='nw', x=170, y=345, height=30, 
                            width=60)
    
    def create_speed_bar(self):
        """ Create a speed bar to control the game speed. """
        self.speed_val = tk.IntVar()
        self.speed_bar = tk.Scale(self, variable=self.speed_val, 
                                orient='horizontal', 
                                label='Game Speed+ Control Bar')
        self.speed_bar.pack()
        self.speed_bar.place(anchor='nw', x=560, y=345, width=224, 
                            height=60)
        self.speed_bar.configure(background='LightCyan2', 
                                activebackground='cyan3')

    def get_text(self, event=None):
        user_input = self.type_in.get()
        print('User has typed ' + user_input)
        self.type_in.delete(0, 'end')
        self.master.update()
        
    def start_game(self, event=None):
        """ Start the game. Method TBD. """
        print("Start Button has been pushed.")
        self.game_start_signal = True

    def close_window(self, event=None):
        self.script.config(state='disabled')
        self.master.update()
        self.master.destroy()

    def window_pause(self, time_t):
        """ this is a function would pause the window. time_t is in
        ms. """
        self.master.after(time_t)

if __name__ == '__main__':
    print('Please import this module to create the application.')