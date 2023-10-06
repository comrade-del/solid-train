from modules.census import census
from modules.functions import create, edit, login

# this is supposed to be in the main.py file
# should I just move to making a webapp instead?
from modules.user import user
from modules.voting import voting

print("Welcome")
print("Menu:")
print("1: Sign up")
print("2: Login")
print("3: Exit")
menu = input("What would you like to do?: ")

if menu == "1":
    user()  # might have to break into two functions for create and edit
elif menu == "2":
    authenticated_user_id = login()  # worked at first try😭😭
    if authenticated_user_id:
        user_id = authenticated_user_id
        while True:
            print("Menu:")
            print("1: Census Form")
            print("2: Voting")
            print("3: Exit")
            page = input("What page would you like to visit? ")
            if page == "1":
                census(user_id)
            elif page == "2":
                voting()
            elif page == "3":
                break
            else:
                print("Invalid option. Please enter a valid choice.")
    else:
        print("Authentication failed. Exiting...")
elif menu == "3":
    pass
else:
    print("Invalid option. Please enter a valid choice.")

