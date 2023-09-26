from pymongo import MongoClient

x = {}
msg = "Success"

client = MongoClient("mongodb://localhost:27017/")
db = client["myapp"]
collection = db["data"]


# collection.insert_one(x)


def edit(x, msg):
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
            try:
                assert x[option]
                new = input(f"Enter new {option}: ")
                _old = {option: x[option]}
                _new = {"$set": {option: new}}
                x[option] = new
                collection.update_one(_old, _new)
                print(msg)
                break
            except KeyError:
                print("Invalid option")


def create(x, msg):
    while True:
        print(x)
        really = input("Is this correct? (Y/N): ")
        if really == "Y".lower():
            collection.insert_one(x)
            print(msg)
            break
        elif really == "N".lower():
            edit(x, msg="Details edited Successfully")
            break
        else:
            print("Invalid option")


for x in collection.find():
    print(x)
