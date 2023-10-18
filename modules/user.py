# User, Password

from modules.functions import create, update, delete_user_data


def user_create():
    print("Welcome")
    user_name = input("User name: ")
    password = input("Password: ")
    user_data = {"user_name": user_name, "password": password, "privilege": "user", "status": "Not Voted"}
    create(user_data, msg="User Added", db="user")


def user_edit(user_id):
    update(user_id, msg="Details edited Successfully", db="user")


def user_delete():
    delete_user_data()
