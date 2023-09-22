# Data collection

from modules.functions import create

print("Welcome to data collection")
print("Please ensure data entered is yours and accurate")

form = dict(first_name=input("First_name: "), surname=input("Surname: "), other_names=input("Other names: "),
            gender=input("Gender: "), dob=input("Date of birth: "))

create(form, msg="Thank you for filling the form")
