from graphviz import Digraph

dot = Digraph('game_flow_parent', filename='game_flow')
dot.attr(label='Game Flow Chart\nby Chao', splines='ortho')

# oval shape for start and end
dot.attr('node', shape='oval')
# first input is label, second input is text on the node
dot.node('start', 'GUI is shown on screen')
dot.node('end', 'GUI is closed')

# box shape for step
dot.attr('node', shape='box')
dot.node('game_started', 'The start game is clicked')
dot.node('welcome_script', 'The welcome script is displayed')

# diamond shape for decisions
dot.attr('node', shape='diamond')
dot.node('new_game_or_not', ('1.Start a new game\n' + 
                            '2.Load from saved players\n' + 
                            '3.User enter other things'))
dot.node('user_io', ('1.Review all players\n' + 
                    '2.Load one player\n' + 
                    '3.Delete one player\n' + 
                    '4.Return to the upper menu'))

# edges
dot.edge('start', 'game_started')
dot.edge('game_started', 'welcome_script')
dot.edge('welcome_script', 'new_game_or_not')
dot.edge('new_game_or_not', 'user_io', xlabel='2')
dot.edge('new_game_or_not', 'new_game_or_not', xlabel='3')
dot.edge('user_io', 'new_game_or_not', xlabel='4')

# child graph for rank level
child = Digraph('game_flow_child')
child.attr(rank='same')

dot.subgraph(child)

dot.view()