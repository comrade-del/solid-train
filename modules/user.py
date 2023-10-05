# User, Password

from modules.functions import create, edit


def user():
    print("Welcome")
    user = {}
    _do = eval(input("What would you like to do?\n1: Add new entry\n2: Edit existing entry\n3: Exit: "))
    while True:
        if _do == 1:
            user = dict(user_name=input("User name: "), password=input("Pass name: "))
            create(user, msg="User Added")
            break
        elif _do == 2:
            edit(user, msg="Details edited Successfully")
            break
        elif _do == 3:
            break
        else:
            print("Invalid option. Type either \"1\", \"2\" or \"3\"")
