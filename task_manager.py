from display import display_all_list_items, get_completion_status
from data import dummy_list
import datetime

def change_item():
    display_all_list_items(dummy_list)
    item_number = int(input("Number of Item you want to change \n >")) - 1
    print('''
    Type "R" to REMOVE the item.
    Type "D" to change the DUE DATE.
    Type "C" to make item as COMPLETE.
    ''')
    change_action = input("> ")
    if change_action.lower() == "r":
        remove_item(item_number)
    elif change_action.lower() == "d":
        new_due_date = input('Enter new due date. (YYYY-MM-DD)')
        dummy_list[item_number][2] = new_due_date
    elif change_action.lower() == "c":
        dummy_list[item_number][3] = True
    else:
        print('Invalid command')
    display_all_list_items(dummy_list)

def remove_item(index):
    del dummy_list[index]
    reindex_items()

def reindex_items():
    for index, item in enumerate(dummy_list):
        item[0] = index + 1

def add_item_to_list():
    task_name = input('Enter Task Description: ')
    due_date = input('Enter Due Date: (YYYY-MM-DD) ')
    dummy_list.append([len(dummy_list) + 1, task_name, due_date, False])
    display_all_list_items(dummy_list)
