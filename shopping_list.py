import os

shopping_list = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_help():
    clear_screen()
    print("What should we pick up at the store? ")
    print("""
    Enter 'DONE' or 'QUIT' to stop adding items.
    Enter 'SHOW' to see your shopping list
    Enter 'HELP' for this help. 
    Enter 'REMOVE' to remove a specific item from your list. """)


def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should we add {}?\n"
                         "Press enter to add to the end of the list.\n"
                         "> ".format(item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position - 1, item)
    else:
        shopping_list.append(item)
    count_of_list = len(shopping_list)
    show_list()


def show_list():
    clear_screen()
    print("Here's your list: ")
    for index, item in enumerate(shopping_list, start=1):
        print('{}. {}'.format(index, item))
    print("-" * 10)


def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove from our shopping list?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()


show_help()

while True:
    new_item = input("- ")
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
    else:
        add_to_list(new_item)

show_list()
