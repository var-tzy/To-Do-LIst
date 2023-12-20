from data import dummy_list, today, current_year, current_month
import calendar
import datetime

def get_completion_status(row):
    return "\033[92mCompleted\033[0m" if row[3] else "\033[91mIncomplete\033[0m"

def get_remaining_time(due_date):
    due_date_obj = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
    delta = due_date_obj - today
    return delta.days if delta.days >= 0 else "Past Due"

def split_task_description(description, max_length=40):
    return [description[i:i+max_length] for i in range(0, len(description), max_length)]

def display_all_list_items(list_to_display):
    header = f"{'Item':<5} | {'Task Description':<40} | {'Due Date':<10} | {'Status':<10} | {'Days Left':<10}"
    print(header)
    print('-' * len(header))
    for i in list_to_display:
        task_chunks = split_task_description(i[1])
        remaining_time = get_remaining_time(i[2])
        for j, chunk in enumerate(task_chunks):
            if j == 0:
                row = f"{i[0]:<5} | {chunk:<40} | {i[2]:<10} | {get_completion_status(i):<10} | {remaining_time:<10}"
            else:
                row = f"{' ':<5} | {chunk:<40} | {' ':<10} | {' ':<10} | {' ':<10}"
            print(row)
            if j == len(task_chunks) - 1:
                print('-' * len(header))

def display_status_report():
    total_tasks = len(dummy_list)
    completed_tasks = sum(1 for item in dummy_list if item[3])
    incomplete_tasks = total_tasks - completed_tasks
    print("\nStatus Report:")
    print(f"\033[94mTotal Tasks: {total_tasks}\033[0m")  # Blue text
    print(f"\033[92mCompleted Tasks: {completed_tasks}\033[0m")  # Green text
    print(f"\033[91mIncomplete Tasks: {incomplete_tasks}\033[0m")  # Red text
    
def display_calendar_with_due_dates():
    cal = calendar.monthcalendar(current_year, current_month)
    due_dates = {datetime.datetime.strptime(item[2], '%Y-%m-%d').day: item[0] for item in dummy_list if datetime.datetime.strptime(item[2], '%Y-%m-%d').month == current_month}
    print("\nCalendar for the Current Month:")
    print(calendar.month_name[current_month], current_year)
    print("Mo Tu We Th Fr Sa Su")
    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end='')
            elif day == today.day:
                print(f"\033[94m{day:2}\033[0m", end=' ')
            elif day in due_dates:
                print(f"\033[91m{day:2}\033[0m", end=' ')
            else:
                print(f"{day:2}", end=' ')
        print()

