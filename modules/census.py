# Data collection

from modules.functions import create, edit

form = {}
print("Welcome to data collection")
print("Please ensure data entered is yours and accurate")
_do = eval(input("What would you like to do?\n1: Add new entry\n2: Edit existing entry\n: "))
# I want to do something to cover dead people too(maybe for admins?)

if _do == 1:
    form = dict(first_name=input("First_name: "), surname=input("Surname: "), other_names=input("Other names: "),
                gender=input("Gender: "), dob=input("Date of birth: "))
    create(form, msg="Thank you for filling the form")
elif _do == 2:
    edit(form, msg="Details edited Successfully")
else:
    print("Invalid option. Type either \"1\" or \"2\"")
