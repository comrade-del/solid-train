# User, Password

from modules.functions import create, edit


def user_create():
    print("Welcome")
    while True:
        user_name = input("User name: ")
        password = input("Password: ")
        user_data = {"user_name": user_name, "password": password, "type": "user"}
        create(user_data, msg="User Added", db="user")


def user_edit(user_id):
    edit(_id=user_id, msg="Details edited Successfully", db="user")
