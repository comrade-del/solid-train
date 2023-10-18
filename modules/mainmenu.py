# this is supposed to be in the main.py file
# should I just move to making a webapp instead?
from modules.census import census
from modules.functions import login
from modules.user import user_edit, user_create, user_delete
from modules.voting import voting

while True:
    print("Welcome")
    print("Menu:")
    print("1: Sign up")
    print("2: Login")
    print("3: Exit")
    menu = input("What would you like to do?: ")

    if menu == "1":
        user_create()
    elif menu == "2":
        result = login()  # worked at first try😭😭
        print(result)  # tuple
        if result:
            user_id, privilege, status = result
            if privilege == "user":
                while True:
                    print("User Menu:")
                    print("1: Census Form")
                    print("2: Voting")
                    print("3: Edit User Details")
                    print("4: Exit")
                    page = input("What page would you like to visit? ")
                    if page == "1":
                        census(user_id, privilege)
                    elif page == "2":
                        voting(user_id, privilege, status)
                    elif page == "3":
                        user_edit(user_id)
                    elif page == "4":
                        break
                    else:
                        print("Invalid option. Please enter a valid choice.")
            elif privilege == "admin":
                while True:
                    print("Admin Menu:")
                    print("1: Census Form")
                    print("2: Voting")
                    print("3: Edit User Details")
                    print("4: Delete User")
                    print("5: Exit")
                    page = input("What page would you like to visit? ")
                    if page == "1":
                        census(user_id, privilege)
                    elif page == "2":
                        voting(user_id, privilege, status)
                    elif page == "3":
                        user_edit(user_id)
                    elif page == "4":
                        user_delete()
                    elif page == "5":
                        break
                    else:
                        print("Invalid option. Please enter a valid choice.")
        else:
            print("Authentication failed. Exiting...")
    elif menu == "3":
        break
    else:
        print("Invalid option. Please enter a valid choice.")
