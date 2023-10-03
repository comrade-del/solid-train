# Data collection

from modules.functions import create, edit


def census(form={}):
    print("Welcome to data collection")
    print("Please ensure data entered is yours and accurate")
    _do = eval(input("What would you like to do?\n1: Add new entry\n2: Edit existing entry\n3: Exit: "))
    while True:
        if _do == 1:
            form = dict(user_name=input("User name: "), password=input("Pass name: "), first_name=input("First name: "),
                        surname=input("Surname: "),
                        other_names=input("Other names: "), gender=input("Gender: "), dob=input("Date of birth: "))
            create(form, msg="Thank you for filling the form")
            break
        elif _do == 2:
            edit(form, msg="Details edited Successfully")
            break
        elif _do == 3:
            break
        else:
            print("Invalid option. Type either \"1\", \"2\" or \"3\"")
