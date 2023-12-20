from menu import show_menu_options, choose_menu_options
from display import display_calendar_with_due_dates, display_all_list_items, display_status_report
from data import dummy_list, today

def start_up():
    print("Today is ", today)  # Display today's date
    display_calendar_with_due_dates()  # Display the calendar with due dates
    print("----------------------")
    print()
    display_all_list_items(dummy_list)
    display_status_report()  # Display the status report
    while True:
        show_menu_options()
        if choose_menu_options():
            break

if __name__ == "__main__":
    start_up()
