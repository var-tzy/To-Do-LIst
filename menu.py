from task_manager import add_item_to_list, change_item
from display import display_all_list_items
from data import dummy_list

def show_menu_options():
    print('''
    Type "A" to ADD a new To Do Item.
    Type "C" to CHANGE an existing item.
    Type "L" to show the LIST. 
    Type "Q" to QUIT.
    ''')

def choose_menu_options():
    add_responses = ['add', 'a', 'new']
    change_responses = ['change', 'c']
    list_responses = ['list', 'l']
    quit_responses = ['q', 'quit', 'exit']
    menu_choice = input('> ')
    if menu_choice.lower() in add_responses:
        add_item_to_list()
    elif menu_choice.lower() in change_responses:
        change_item()
    elif menu_choice.lower() in list_responses:
        display_all_list_items(dummy_list)
    elif menu_choice.lower() in quit_responses:
        return True
    else:
        print('Not a menu option.')
        show_menu_options()
    return False
