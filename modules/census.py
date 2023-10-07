# Data collection

from modules.functions import create, edit


def census(user_id):
    print("Welcome to data collection")
    print("Please ensure data entered is yours and accurate")
    form = {}
    while True:
        _do = eval(input("What would you like to do?\n1: Add new entry\n2: Edit existing entry\n3: Exit: "))
        if _do == 1:
            form = dict(_id=user_id, first_name=input("First name: "), surname=input("Surname: "),
                        other_names=input("Other names: "), gender=input("Gender: "), dob=input("Date of birth: "))
            create(form, msg="Thank you for filling the form")
        elif _do == 2:
            edit(_id=user_id, msg="Details edited Successfully", db="census")
        elif _do == 3:
            break
        else:
            print("Invalid option. Type either \"1\", \"2\" or \"3\"")

# Example usage of the census function with a user_id:
# census(some_user_id)
