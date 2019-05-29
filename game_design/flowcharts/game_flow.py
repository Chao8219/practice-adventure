from graphviz import Digraph

dot = Digraph('game_flow_parent', filename='game_flow')
dot.attr(label='Game Flow Chart\nby Chao', splines='ortho')

# oval shape for start and end
dot.attr('node', shape='oval')
# first input is label, second input is text on the node
dot.node('start', 'GUI appears')
dot.node('end', 'GUI distroys\ngame ends')

# soild box shape for whatever could be seen on the GUI
dot.attr('node', shape='box', style='solid')
dot.node('game_started', 'The start game button\nis clicked')
dot.node('welcome_script', 'Display welcome script')
dot.node('enter_yourname', 'User enter his/her name')
dot.node('display_player_status', ('Player\'s status is\n' + 
    'displayed on the right'))
dot.node('game_main_script', 'The game starts from beginning')

# dotted box shpae for whatever is under the GUI, 
# could not be seen by user
dot.attr('node', shape='box', style='dotted')
dot.node('create_db_file', 'Create db file')
dot.node('get_new_player', ('Generate a\n' + 
    'new player object'))

# diamond shape for decisions
dot.attr('node', shape='diamond', style='solid')
user_enter_random = 'www: user enter other things'
dot.node('check_db_file', 'Check if db file exists')
dot.node('new_game_or_not', ('1.Start a new game\n' + 
    '2.Load from saved players\n' + 
    user_enter_random))
dot.node('user_io', ('1.Review all players\n' + 
    '2.Load one player\n' + 
    '3.Delete one player\n' + 
    '4.Return to the upper menu\n' + 
    user_enter_random))
dot.node('player_data_check1', 'See if the name exists\nin the db file')

# edges
dot.edge('start', 'game_started')
dot.edge('game_started', 'check_db_file')
dot.edge('check_db_file', 'create_db_file', xlabel='No')
dot.edge('create_db_file', 'welcome_script')
dot.edge('check_db_file', 'welcome_script', xlabel='Yes')
dot.edge('welcome_script', 'new_game_or_not')
dot.edge('new_game_or_not', 'enter_yourname', xlabel='1')
dot.edge('enter_yourname', 'player_data_check1')
dot.edge('player_data_check1', 'enter_yourname', xlabel='Yes')
dot.edge('player_data_check1', 'get_new_player', xlabel='No')
dot.edge('get_new_player', 'display_player_status')
dot.edge('display_player_status', 'game_main_script')
dot.edge('new_game_or_not', 'user_io', xlabel='2')
dot.edge('new_game_or_not', 'new_game_or_not', xlabel='www')
dot.edge('user_io', 'new_game_or_not', xlabel='4')
dot.edge('game_main_script', 'end')

# child graph for rank level
child = Digraph('game_flow_child')
child.attr(rank='same')

dot.subgraph(child)

dot.view()