# Data collection

from modules.functions import create, update


def census(user_id, privilege):
    print("Welcome to data collection")
    print("Please ensure data entered is yours and accurate")
    while True:
        if privilege == "user":
            _do = eval(input("What would you like to do?\n1: Add new entry\n2: Update existing entry\n3: Exit: "))
            if _do == 1:
                form = dict(_id=user_id, firstname=input("First name: "), surname=input("Surname: "),
                            othernames=input("Other names: "), gender=input("Gender: "), dob=input("Date of birth: "))
                create(form, msg="Thank you for filling the form", db="census")
            elif _do == 2:
                update(_id=user_id, msg="Details edited Successfully", db="census")
            elif _do == 3:
                break
            else:
                print("Invalid option. Type either \"1\", \"2\" or \"3\"")
        elif privilege == "admin":
            _do = eval(input("What would you like to do?\n1: Add new entry\n2: Update existing entry\n3: Delete existing entry\n4: Exit: "))
            if _do == 1:
                form = dict(_id=user_id, firstname=input("First name: "), surname=input("Surname: "),
                            othernames=input("Other names: "), gender=input("Gender: "), dob=input("Date of birth: "))
                create(form, msg="Thank you for filling the form", db="census")
            elif _do == 2:
                update(_id=user_id, msg="Details edited Successfully", db="census")
            elif _do == 3:
                pass  # delete function
            elif _do == 4:
                break
            else:
                print("Invalid option. Type either \"1\", \"2\" or \"3\"")
