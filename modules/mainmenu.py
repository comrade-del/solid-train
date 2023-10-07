from modules.census import census
from modules.functions import login

# this is supposed to be in the main.py file
# should I just move to making a webapp instead?
from modules.user import user_edit, user_create
from modules.voting import voting

print("Welcome")
print("Menu:")
print("1: Sign up")
print("2: Login")
print("3: Exit")
menu = input("What would you like to do?: ")

if menu == "1":
    user_create()
elif menu == "2":
    authenticated_user_id = login()  # worked at first try😭😭
    if authenticated_user_id:
        user_id = authenticated_user_id
        while True:
            print("Menu:")
            print("1: Census Form")
            print("2: Voting")
            print("3: Edit User Details")
            print("4: Exit")
            page = input("What page would you like to visit? ")
            if page == "1":
                census(user_id)
            elif page == "2":
                voting()
            elif page == "3":
                user_edit(user_id)
            elif page == "4":
                break
            else:
                print("Invalid option. Please enter a valid choice.")
    else:
        print("Authentication failed. Exiting...")
elif menu == "3":
    pass
else:
    print("Invalid option. Please enter a valid choice.")

