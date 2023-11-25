from my_functions.classes import Item
from my_functions.reports import table_report

def choose_action(menu):
    print("Choose action!")
    if menu == 'main menu':
        action = input("1 - Work with articles, 2 - Reports, 0 - Exit: ")
    elif menu == 'articles':
        action = input('1 - Add new article, 2 - Change article, 3 - Delete article, 9 - Main menu, 0 - Exit: ')
    elif menu == 'reports':
        action = input('1 - Full table report, 2 - Filtered table report,  9 - Maim menu, 0 - Exit: ')
    return action


def main_menu():
    while True:
        action = choose_action('main menu')
        if action == '1':
            work_with_articles()
        elif action == '2':
            work_with_reports()
        elif action == '0':
            exit_system()
        else:
            print('Incorrect answer. Fill in "1", "2" or "0"')

def work_with_articles():
    while True:
        action = choose_action('articles')
        if action == '1': #Add new article
            Item.add_neu_item()
        elif action == '2': #Change article
            Item.change_item()
        elif action == '3': #Delete article
            Item.delete_item()
        elif action == '9':
            main_menu()
        elif action == '0':
            exit_system()
        else:
            print("Incorrect answer")

def work_with_reports():
    while True:
        action = choose_action('reports')
        if action == '1':
            table_report()
        elif action == '2':
            print("under development :)")
            # table_report(True)
        elif action == '9':
            main_menu()
        elif action == '0':
            exit_system()
        else:
            print("Incorrect answer")

def exit_system():
    print("Good by!")
    raise SystemExit


def save_data_question(ask_question=False, delete_data=False):
    if ask_question:
        if delete_data:
            answer = input("Do you really want to delete element? Yes - 1, No - any other key: ")
        else:  # change article
            answer = input("Save changes? Yes - 1, No - any other key: ")
        if answer == "1":
            return True
        else:
            return False
    else:  # add new article
        return True


def delete_data_question():
    answer = input("Do you really want to delete element? Yes - 1, No - any other key: ")
    if answer == "1":
        return True
    else:
        return False

