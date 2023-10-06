# User, Password

from modules.functions import create, edit


def user():
    print("Welcome")
    while True:
        _do = eval(input("What would you like to do?\n1: Add new entry\n2: Edit existing entry\n3: Exit: "))
        if _do == 1:
            user_name = input("User name: ")
            password = input("Password: ")
            user_data = {"user_name": user_name, "password": password}
            create(user_data, msg="User Added")
        elif _do == 2:
            user_name = input("User name: ")
            password = input("Password: ")
            user_data = {"user_name": user_name, "password": password}
            edit(user_data, msg="Details edited Successfully")
        elif _do == 3:
            break
        else:
            print("Invalid option. Type either \"1\", \"2\" or \"3\"")

# Example usage of the user function:
# user()
