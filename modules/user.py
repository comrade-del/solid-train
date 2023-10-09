# User, Password

from modules.functions import create, update


def user_create():
    print("Welcome")
    user_name = input("User name: ")
    password = input("Password: ")
    user_data = {"user name": user_name, "password": password, "privilege": "user"}
    create(user_data, msg="User Added", db="user")


def user_edit(user_id):
    update(_id=user_id, msg="Details edited Successfully", db="user")


def user_delete(privilege):
    pass  # delete function
