import tkinter as tk
from tkinter import ttk

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
    hp_value = 100

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
        self.create_health_bar()
        self.create_info_frame()
        self.create_wear_frame()

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
    
    def create_health_bar(self):
        """ Create a health points bar to display the current HP"""
        theme_setting = ttk.Style()
        theme_setting.theme_use('classic') 
        #('aqua', 'clam', 'alt', 'default', 'classic') are the choices
        theme_setting.configure("HP.Horizontal.TProgressbar", 
                            troughcolor='SteelBlue1', 
                            background='pale green')

        self.hp_frame = tk.Frame(self, background='LightCyan2')
        self.hp_frame.pack()
        self.hp_frame.place(anchor='ne', x=550, y=345, width=160, 
                        height=60)

        self.hp_label1 = tk.Label(self.hp_frame, text='HP', bd=4, 
                                background='LightCyan2')
        self.hp_label1.pack()
        self.hp_label1.place(anchor='nw', x=0, y=0)

        self.hp_bar = ttk.Progressbar(self.hp_frame, orient='horizontal', 
                                    length=150, mode='determinate')
        self.hp_bar.pack()
        self.hp_bar.config(value=self.hp_value, 
                        style='HP.Horizontal.TProgressbar')
        self.hp_bar.place(anchor='n', x=80, y=30)

        self.hp_val_label = tk.Label(self.hp_frame, bd=4, 
                                    background='LightCyan2')
        self.hp_val_label.pack()
        self.hp_val_label.configure(text=str(self.hp_value)+'/100')
        self.hp_val_label.place(anchor='ne', x=160, y=0)

    def create_info_frame(self):
        """ Create player's info frame. """
        self.info_frame = tk.Frame(self, relief='groove')
        self.info_frame.pack()
        self.info_frame.place(anchor='nw', x=560, y=10, height=190, 
                            width=224)
        self.info_frame.configure(background='LightCyan2')
        self.create_info_name()
    
    def create_info_name(self):
        """ Create the info name to display the player's name. """
        self.info_name_up = tk.Label(self.info_frame, text="Your Name", 
                                background='LightCyan2')
        self.info_name_up.pack()
        self.info_name_up.place(anchor='n', x=112, y=10)

        self.info_name_down = tk.Label(self.info_frame, 
                                    background='LightCyan2')
        self.info_name_down.pack()
        self.info_name_down.place(anchor='n', x=112, y=30)
    
    def create_status_frame(self):
        self.status_frame = tk.Frame(self.info_frame, 
                                    background='LightCyan2')
        self.status_frame.pack()
        self.status_frame.place(anchor='n', x=112, y=55, height=125, 
                            width=170)
        self.create_status_widgets()
    
    def create_status_widgets(self):
        self.status_name = tk.Listbox(self.status_frame, bd=0, 
                                    background='LightCyan2')
        self.status_name.pack()
        self.status_name.place(anchor='nw', x=0, y=0, height=125, width=65)
        self.status_name.insert(1,'Strenth ')
        self.status_name.insert(2,'Intellect ')
        self.status_name.insert(3,'Agility ')
        self.status_name.insert(4,'Defense ')
        self.status_name.insert(5,'Faith ')
        self.status_name.insert(6,'Sanity ')
        self.status_name.insert(7,'Luck ')
        self.status_name.config(justify='right')

        self.status_val = tk.Listbox(self.status_frame, bd=0, 
                                    background='LightCyan2')
        self.status_val.pack()
        self.status_val.place(anchor='n', x=100, y=0, height=125, 
                            width=40)
        self.status_val.config(justify='center')
        for i in range(0,7):
            self.status_val.insert(i, '0')

        self.status_addval = tk.Listbox(self.status_frame, bd=0, 
                                    background='LightCyan2')
        self.status_addval.pack()
        self.status_addval.place(anchor='ne', x=160, y=0, height=125, 
                                width=40)
        self.status_addval.config(justify='center')
        for i in range(0,7):
            self.status_addval.insert(i, '+0')
    
    def create_wear_frame(self):
        self.wear_frame = tk.Frame(self, relief='groove')
        self.wear_frame.pack()
        self.wear_frame.place(anchor='nw', x=560, y=210, height=120, 
                            width=224)
        self.wear_frame.configure(background='LightCyan2')
        self.create_wears()
    
    def create_wears(self):
        self.wear_frame_name = tk.Label(self.wear_frame, text="Equipment", 
                                    background='LightCyan2')
        self.wear_frame_name.pack()
        self.wear_frame_name.place(anchor='n', x=112, y=5)

        self.headwear = tk.Label(self.wear_frame, text="Headwear", 
                                background='LightCyan2')
        self.headwear.pack()
        self.headwear.place(anchor='n', x=50, y=30)

        self.headwear2 = tk.Label(self.wear_frame, background='LightCyan2', 
                                text='None')
        self.headwear2.pack()
        self.headwear2.place(anchor='n', x=50, y=50)

        self.armour = tk.Label(self.wear_frame, text="Armour", 
                            background='LightCyan2')
        self.armour.pack()
        self.armour.place(anchor='n', x=174, y=30)

        self.armour2 = tk.Label(self.wear_frame, background='LightCyan2', 
                            text='None')
        self.armour2.pack()
        self.armour2.place(anchor='n', x=174, y=50)

        self.weapon = tk.Label(self.wear_frame, text="Weapon", 
                            background='LightCyan2')
        self.weapon.pack()
        self.weapon.place(anchor='n', x=50, y=70)

        self.weapon2 = tk.Label(self.wear_frame, background='LightCyan2', 
                            text='None')
        self.weapon2.pack()
        self.weapon2.place(anchor='n', x=50, y=90)

        self.footwear = tk.Label(self.wear_frame, text="Footwear", 
                                background='LightCyan2')
        self.footwear.pack()
        self.footwear.place(anchor='n', x=174, y=70)

        self.footwear2 = tk.Label(self.wear_frame, background='LightCyan2', 
                                text='None')
        self.footwear2.pack()
        self.footwear2.place(anchor='n', x=174, y=90)
   
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