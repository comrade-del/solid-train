from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

x = {}
msg = "Success"
user_id = None
_id = None

client = MongoClient("mongodb://localhost:27017/")
db = client["myapp"]
collection = db["data"]
usercol = db["user"]


# collection.insert_one(x)


def edit(_id, msg, db):  # will make separate for update
    who = {"_id": _id}
    if db == "census":
        x = collection.find_one(who)
    elif db == "user":
        x = usercol.find_one(who)
    while True:
        # x = collection.find_one()
        # for x in collection.find():
        # print(x) will introduce properly when I fix in sign up and log in
        print(x)
        print("What would you like to edit\nType \"exit\" if you changed your mind")
        option = input(": ").lower()
        if "vote" in option:
            print("Are you trying to rig elections?")
        elif option == "exit":
            print("Okay")
            break
        else:
            collection.find_one(who)
            try:
                assert x[option]
                new = input(f"Enter new {option}: ")
                _old = {option: x[option]}
                _new = {"$set": {option: new}}
                x[option] = new
                if db == "census":
                    collection.update_one(_old, _new)
                elif db == "user":
                    usercol.update_one(_old, _new)
                print(msg)
                break
            except KeyError:
                print("Invalid option")


def create(x, msg):
    while True:
        print(x)
        really = input("Is this correct? (Y/N): ")
        if really == "Y".lower():
            db = input("add where?: ")
            if db == "user".lower():
                u = usercol.insert_one(x)
                user_id = u.inserted_id
                print(msg)
                # print(f'Your ID is {user_id}')  # works, just need to work out custom IDs in my head
            elif db == "census".lower():
                try:
                    c = collection.insert_one(x)
                    print(msg)
                except DuplicateKeyError:
                    print("You already have an entry. Maybe you mean edit?")

            elif db == "voting".lower():
                # print(msg)
                pass  # will create a database for voters if users works
            else:
                print("No such database")
            break
        elif really == "N".lower():
            edit(x, msg="Details edited Successfully")
        else:
            print("Invalid option")


"""try:
        # Attempt to insert a new user document
        collection.insert_one({"user_name": user_name, "password": password})
        print("User created successfully.")
    except DuplicateKeyError:
        print("Username already exists. Please choose a different username.")"""


def login():
    user = input("Name?: ")
    password = input("Password?: ")
    who = {"user_name": user, "password": password}
    authenticated_user = usercol.find_one(who)
    if authenticated_user:
        return authenticated_user["_id"]  # Return the user_id of the authenticated user
    else:
        return None  # Return None if authentication fails


# for x in collection.find():
# print(x)
# user = input("Name?: ")
# password = input("Password?: ")
# who = {"user_name": user, "password": password}
# x = usercol.find_one(who)
# print(x)
# user = input("Name?: ")
# who = {"surname": user}
# w = collection.find(who)
# if w:
# print("yey")  # works, can use

# mydict = { "name": "Peter", "address": "Lowstreet 27" }

# x = collection.insert_one(mydict)

# print(x.inserted_id)
# for x in collection.find():
# print(x)
# print(x.inserted_id)
