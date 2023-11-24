# from my_functions.files import write_file
# from my_functions.reports import *
from my_functions.classes import Item
from my_functions.client import Client

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
        if action == '1':
            new_article = Item.add_neu_item()
            if new_article != None:
                Client.addArticle(new_article)
            # my_wardrobe.add_new_item()
        # elif action == '2':
        #     my_wardrobe.change_item()
        # elif action == '3':
        #     my_wardrobe.delete_item()
        elif action == '9':
            main_menu()
        elif action == '0':
            exit_system()
        else:
            print("Incorrect answer")

# def main_menu(my_wardrobe):
#     while True:
#         action = choose_action('main menu')
#         if action == '1':
#             work_with_articles(my_wardrobe)
#         elif action == '2':
#             work_with_reports(my_wardrobe)
#         elif action == '0':
#             exit_system(my_wardrobe)
#         else:
#             print('Incorrect answer. Fill in "1", "2" or "0"')

# def work_with_articles(my_wardrobe):
#     while True:
#         action = choose_action('articles')
#         if action == '1':
#             my_wardrobe.add_new_item()
#         elif action == '2':
#             my_wardrobe.change_item()
#         elif action == '3':
#             my_wardrobe.delete_item()
#         elif action == '9':
#             main_menu(my_wardrobe)
#         elif action == '0':
#             exit_system(my_wardrobe)
#         else:
#             print("Incorrect answer")


def work_with_reports(my_wardrobe):
    while True:
        action = choose_action('reports')
        if action == '1':
            table_report(my_wardrobe)
        elif action == '2':
            table_report(my_wardrobe, True)
        elif action == '9':
            main_menu(my_wardrobe)
        elif action == '0':
            exit_system(my_wardrobe)
        else:
            print("Incorrect answer")


def exit_system():
    # answer = input("Save changes made in session? Yes - 1, No - any other key: ")
    # if answer == "1":
    #     #write_file("wardrobe.csv", my_wardrobe)
    #     write_data(my_wardrobe)
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

# class Client():
#
#     backendAddress = "http://localhost:7000/articles"
#
#     @staticmethod
#     def addArticle(article):
#         result = requests.post(
#                 Client.backendAddress,
#                 json=article.dict())
#         return result
