import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
import user_io
import player_class

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
    enter_signal = False
    user_input = ''
    
    def __init__(self, path, file, master=None):
        super().__init__(master)
        self.master = master
        self.path = path
        self.file = file
        self.pack(anchor='w', fill='both', expand='1')
        # create a void player object
        self.player_obj = player_class.CreatePlayer('Void')
        self.create_widgets()
        while self.game_start_signal is False:
            self.master.update()
        self.welcome_screen()
        self.main_scripts()
        
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
        script_helv10 = tkfont.Font(family='Helvetica', size=10)
        self.script = tk.Text(self, font=script_helv10, 
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
        button_helv10 = tkfont.Font(family='Helvetica', size=10)
        self.start_button = tk.Button(self, text='Start Game', 
                                    font=button_helv10, 
                                    command=self.start_game)
        self.start_button.pack()
        self.start_button.place(anchor='nw', x=10, y=385, height=30, 
                            width=90)
    
    def create_exit_button(self):
        button_helv10 = tkfont.Font(family='Helvetica', size=10)
        exit_button = tk.Button(self, text='Exit', font=button_helv10,
                            command=self.close_window)
        exit_button.pack()
        exit_button.place(anchor='nw', x=110, y=385, height=30, width=60)

    def create_enter_button(self):
        """ Create a enter button to give users a alternative to submit
        what they have entered in the Entry widget. """
        button_helv10 = tkfont.Font(family='Helvetica', size=10)
        self.enter_button = tk.Button(self, text='Enter', 
                                    font=button_helv10, 
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
        self.create_status_frame()
    
    def create_info_name(self):
        """ Create the info name to display the player's name. """
        self.info_yourname = tk.Label(self.info_frame, text="Your Name", 
                                background='LightCyan2')
        self.info_yourname.pack()
        self.info_yourname.place(anchor='n', x=112, y=10)

        self.display_player_name = tk.Label(self.info_frame, 
                                    background='LightCyan2')
        self.display_player_name.pack()
        self.display_player_name.place(anchor='n', x=112, y=30)
    
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
        self.status_name.insert(1, 'Strenth ')
        self.status_name.insert(2, 'Intellect ')
        self.status_name.insert(3, 'Agility ')
        self.status_name.insert(4, 'Defense ')
        self.status_name.insert(5, 'Faith ')
        self.status_name.insert(6, 'Sanity ')
        self.status_name.insert(7, 'Luck ')
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
        self.user_input = self.type_in.get()
        print('User has typed ' + self.user_input)
        self.enter_signal = True
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

    def print_name(self, a_name):
        """ Print the name before each line. """
        self.enter_signal = False
        # with new line, the user is not entering
        self.type_in.config(state='disabled')
        # not allowed entering between lines
        self.enter_button.config(state='disabled')
        the_name = a_name + ': '
        for i in range(0, len(the_name)):
            self.script.config(state='normal')
            self.script.insert('end', the_name[i])
            self.master.update()
            self.script.see('end') # auto scroll the scrollbar
            self.script.config(state='disabled')
            self.reduce_speed() # delay 70 ms by default
            self.master.update()
        self.window_pause(400)
        self.master.update()
        self.type_in.config(state='normal')
        self.enter_button.config(state='normal')

    def print_line(self, a_line):
        self.enter_signal = False
        # with new line, the user is not entering
        self.type_in.config(state='disabled') 
        # not allowed entering between lines
        self.enter_button.config(state='disabled')
        for i in range(0, len(a_line)):
            self.script.config(state='normal')
            self.script.insert('end', a_line[i])
            self.master.update()
            self.script.see('end') # auto scroll the scrollbar
            self.script.config(state='disabled')
            self.reduce_speed() # delay 70 ms by default
            self.master.update()
        self.window_pause(400)
        self.master.update()
        self.type_in.config(state='normal')
        self.enter_button.config(state='normal')
    
    def quick_print(self, words):
        self.enter_signal = False
        # with new line, the user is not entering
        self.type_in.config(state='disabled') 
        # not allowed entering between lines
        self.enter_button.config(state='disabled')
        self.script.config(state='normal')
        self.script.insert('end', words)
        self.master.update()
        self.script.see('end') # auto scroll the scrollbar
        self.script.config(state='disabled')
        self.master.update()
        self.window_pause(400)
        self.master.update()
        self.type_in.config(state='normal')
        self.enter_button.config(state='normal')

    def reduce_speed(self):
        ass = 0
        ass = 100 - int(self.speed_val.get())
        self.window_pause(ass)
    
    def wait_for_input(self):
        while(self.enter_signal is False):
            self.master.update()

    def clean_user_input(self):
        self.enter_signal = False
        self.user_input = ''

    def welcome_screen(self):
        self.print_line('Hey, how are you doing today?' + '\n')
        self.print_line('Welcome to play!' + '\n')
        self.print_line('This is a demo for apps and games' + 
                    ' that is based on tkinter. ' + '\n')
        self.print_line('You will see some basic ideas about' + 
                    ' my games, e.g. player\'s data access,' + 
                    ' basic game attributes.' + '\n')
        self.print_line('Please allow me to exam the game database' + 
                    ' status...\n')
        # create path and file if there is none
        if user_io.create_file(self.path, self.file) is False:
            self.print_line('Game data file exists.\n')
        else:
            self.print_line('Game data file is created successfully.\n\n')
        while True:
            self.print_line('Would you like to:' + '\n')
            self.quick_print('  1. Start as a new player.\n' + 
                            '  2. Load from saved player list\n')
            self.wait_for_input()
            temp_input = self.user_input
            self.clean_user_input()
            if temp_input == '1':
                self.create_new_player()
                break
            elif temp_input == '2':
                main_menu_signal = self.save_n_load()
                if main_menu_signal == False:
                    break
                else:
                    pass
            else:
                self.quick_print('Please only enter 1 or 2.\n')
    
    def save_n_load(self):
        """ This method is main user io method"""
        main_menu_signal = False
        while True:
            self.print_line('Please select:\n')
            self.quick_print('  1. Review saved players list.\n')
            self.quick_print('  2. Load one player.\n')
            self.quick_print('  3. Delete one player.\n')
            self.quick_print('  4. Return to the main menu.\n')
            self.wait_for_input()
            temp_input = self.user_input
            self.clean_user_input()
            if temp_input == '1':
                if self.save_n_load_1() is False:
                    self.quick_print('There is no saved ' + 
                                        'player in the db file.\n')
                else:
                    pass
            elif temp_input == '2':
                player_obj = self.save_n_load_2()
                if player_obj is False:
                    pass
                else:
                    self.quick_print('Welcome back, ' + player_obj.name + 
                                        '!\n')
                    self.player_obj = player_obj
                    main_menu_signal = False
                    return main_menu_signal
            elif temp_input == '3':
                # if return is True, it means the file is deleted
                self.save_n_load_3()
            elif temp_input == '4':
                main_menu_signal = True
                return main_menu_signal
            else:
                # stay inside this while loop
                self.quick_print('Please select between 1 to 4.\n')

    def save_n_load_1(self):
        # check if the db file has any player data
        if user_io.empty_check(self.file) is True:
            return False
        obtained_all_player_info = user_io.read_all(self.file)
        self.quick_print('Saved Player List:\n')
        for j in range(0, len(obtained_all_player_info)):
            self.quick_print(' ' + obtained_all_player_info[j][0] + 
                            '\n')
        self.clean_user_input()
        while True:
            self.quick_print('Please select one name to see details.' + 
                'Or enter 2 to return the upper menu.\n')
            self.wait_for_input()
            temp_input = self.user_input
            self.clean_user_input()
            if temp_input == '2':
                break
            elif user_io.find_info(temp_input, self.file) is False:
                self.quick_print('No such a name. \n')
            else:
                self.quick_print('Found it! Please see player' + 
                                'status for details.\n')
                player_obj = user_io.read_one(temp_input, self.file)
                self.update_status_display(player_obj)
                break
        return True
    
    def save_n_load_2(self):
        if user_io.empty_check(self.file) is True:
            self.quick_print('There is no saved player.\n')
            return False
        while True:
            self.quick_print('Please enter the name you want to load.' + 
                'Or enter 2 to return the upper menu.\n')
            self.wait_for_input()
            temp_input = self.user_input
            self.clean_user_input()
            if temp_input == '2':
                break
            elif user_io.find_info(temp_input, self.file) is False:
                self.quick_print('No such a name. \n')
            else:
                player_obj = user_io.read_one(temp_input, self.file)
                self.update_status_display(player_obj)
                return player_obj

    def save_n_load_3(self):
        if user_io.empty_check(self.file) is True:
            self.quick_print('There is no saved player.\n')
            return False
        while True:
            self.quick_print('Please enter the name you want to delete.' + 
                'Or enter 2 to return the upper menu.\n')
            self.wait_for_input()
            temp_input = self.user_input
            self.clean_user_input()
            if temp_input == '2':
                break
            elif user_io.find_info(temp_input, self.file) is False:
                self.quick_print('No such a name. \n')
            else:
                name_to_be_deleted = temp_input
                self.quick_print('Found the name. ' + 
                    'Do you really want to delete it? ' + 
                    'There is no way to get them back after deleted.' + 
                    'If you are certain, please enter \'yes\' to ' + 
                    'perform. Or type in other words to return ' + 
                    'the upper menu.\n')
                self.wait_for_input()
                temp_input = self.user_input
                self.clean_user_input()
                if (temp_input == 'yes' or 
                    temp_input == 'Yes' or 
                    temp_input == 'YES'):
                    user_io.delete_info(name_to_be_deleted, self.file)
                    self.quick_print('Player data deleted.\n')
                    return True
                else:
                    self.quick_print('Return to the upper menu.\n')
                    return False

    def update_status_display(self, player_obj):
        self.display_player_name.config(text=player_obj.name)
        self.status_val.delete(0, 'end') # clear listbox
        for j in range(0, 7):
            self.status_val.insert(j+1, int(player_obj.attr[0, j]))
        self.headwear2.config(text=player_obj.armor[0])
        self.armour2.config(text=player_obj.armor[1])
        self.weapon2.config(text=player_obj.armor[2])
        self.footwear2.config(text=player_obj.armor[3])
    
    def create_new_player(self):
        while True:
            self.quick_print('Please enter a name for the new player.\n')
            self.wait_for_input()
            temp_input = self.user_input
            self.clean_user_input()
            if user_io.find_info(temp_input, self.file) is True:
                self.quick_print('The name exists in the db file. ' + 
                    'Please re-enter the name.\n')
                continue
            elif temp_input.isdigit():
                self.quick_print('Please avoid using pure number.\n')
                continue
            else:
                player_obj = player_class.CreatePlayer(temp_input)
                user_io.insert_info(player_obj, self.file)
                self.update_status_display(player_obj)
                self.quick_print('Player is created!\n')
                self.player_obj = player_obj
                break

    def monster_action(self, monster_name, monster_move):
        words = ('A ' + monster_name + ' ' + monster_move + '!\n')
        script_helv10_bold = tkfont.Font(family='Helvetica', size=10, 
                                            weight='bold')
        self.enter_signal = False
        # with new line, the user is not entering
        self.type_in.config(state='disabled') 
        # not allowed entering between lines
        self.enter_button.config(state='disabled')
        self.script.config(state='normal')
        self.script.insert('end', words)
        insert_loc = self.script.index(tk.INSERT)
        insert_line_num = str(int(float(insert_loc)) - 1)
        word_start_index = insert_line_num + '.0'
        word_end_index = insert_line_num + '.' + str(len(words) - 1)
        self.script.tag_add('current_line', word_start_index, 
                            word_end_index)
        self.script.tag_config('current_line', font=script_helv10_bold, 
                                justify='center')
        self.master.update()
        self.script.see('end') # auto scroll the scrollbar
        self.script.config(state='disabled')
        self.master.update()
        self.window_pause(400)
        self.master.update()
        self.type_in.config(state='normal')
        self.enter_button.config(state='normal')

    def main_scripts(self, host_name='Alex'):
        self.print_name(host_name)
        self.print_line('Hello there, my name is ' + host_name + 
                        ' , welcome to take an adventure in our world.\n')
        self.print_name(host_name)
        self.print_line('As a new comer to this world, ' + 
                        'you may wonder how everything works. ' + 
                        'Please allow me to introduce things to you.\n')
        self.print_name(host_name)
        self.print_line('On the left, it\'s the main script frame, ' + 
                        'where you can see how the game runs.\n' + 
                        'On the right, you may check your role\'s ' + 
                        'status and equipments that will affect ' + 
                        'if you are able to survive through the ' + 
                        'journey.\n')
        self.print_name(host_name)
        self.print_line('Of course, you will encounter some foul ' + 
                        'creatures. A powerful weapon may assist ' + 
                        'you to defeat them.\n')
        self.print_name(host_name)
        self.print_line('Speaking of which, a sneaky goblin, the ' + 
                        'most common fool monster, is approching ' + 
                        'us. Are you ready to give it a shot?\n')
        self.monster_action('goblin', 'shows up')

if __name__ == '__main__':
    print('Please import this module to create the application.')