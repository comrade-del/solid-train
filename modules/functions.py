from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

x = {}
msg = "Success"
user_id = None
_id = None

client = MongoClient("mongodb://localhost:27017/")
db = client["myapp"]
census = db["data"]
users = db["user"]
# users.create_index("user_name", unique=True)  # will unleash after dropping, might not even be useful again
voting = db["voting"]


def update(_id, msg, db):  # will make separate for update
    while True:
        who = {"_id": _id}
        if db == "census":
            x = census.find_one(who)
            print(x)
            if x is None:
                print("You have not filled the form")
                break
        elif db == "user":
            x = users.find_one(who)
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
                if db == "census":
                    census.update_one(_old, _new)
                elif db == "user":
                    users.update_one(_old, _new)
                print(msg)
                break
            except KeyError:
                print("Invalid option")


def edit(x):
    print(x)
    print("What would you like to edit\nType \"exit\" if you changed your mind")
    option = input(": ").lower()
    try:
        assert x[option]
        new = input(f"Enter new {option}: ")
        x[option] = new
        # print(msg)
    except KeyError:
        print("Invalid option")


def create(x, msg, db):
    while True:
        print(x)
        really = input("Is this correct? (Y/N): ")
        if really == "Y".lower():
            if db == "user".lower():
                users.insert_one(x)
                print(msg)
            elif db == "census".lower():
                try:
                    census.insert_one(x)
                    print(msg)
                except DuplicateKeyError:
                    print("You already have an entry. Maybe you mean update?")
            elif db == "voting".lower():
                voting.insert_one(x)
                print(msg)
                pass  # will create a database for voters if users works
            else:
                print("No such database")
            break
        elif really == "N".lower():
            edit(x)
        else:
            print("Invalid option")


def login():
    user = input("Name?: ")
    password = input("Password?: ")
    who = {"user_name": user, "password": password}
    authenticated_user = users.find_one(who)
    if authenticated_user:
        privilege = authenticated_user.get("privilege")
        status = authenticated_user.get("status")
        return authenticated_user[
                   "_id"], privilege, status  # Return the user_id and privilege of the authenticated user
    else:
        return None  # Return None if authentication fails


def vote(_id, party):
    voter = {"_id": _id}
    vodetails = users.find_one(voter)
    before = vodetails.get("status")
    after = "Voted"
    _olds = {"status": before}
    _news = {"$set": {"status": after}}
    who = {"party": party}
    candetails = voting.find_one(who)
    vote = candetails.get("vote_count")
    votes = vote + 1
    _old = {"vote_count": vote}
    _new = {"$set": {"vote_count": votes}}
    voting.update_one(_old, _new)
    users.update_one(_olds, _news)
    print("Thank you for voting")


def showv():
    c = voting.find({}, {"_id": 0, "party": 1})
    for i, c in enumerate(c, start=1):
        print(f"{i}. {c['party']}")


def voteres():
    c = voting.find({}, {"_id": 0, "party": 1, "vote_count": 1})
    for i, c in enumerate(c, start=1):
        print(f"{i}. {c['party']}, {c['vote_count']}")


def delete_user_data():
    try:
        u = users.find({"privilege": "user"}, {"_id": 0, "user_name": 1})
        users_dict = {}
        for i, doc in enumerate(u, start=1):
            user_name = doc.get('user_name')
            if user_name:
                users_dict[i] = user_name

        if not users_dict:
            print("No user data found.")
            return

        for i, p in enumerate(users_dict, start=1):
            print(f'{i}. {users_dict[i]}')

        w = int(input("Select one: "))

        if w in users_dict:
            s = users_dict[w]
            user = users.find_one({"user_name": s})

            if user:
                user_id = user["_id"]
                census.delete_one({"user_id": user_id})
                # then subtract one from vote_count, too tasking
                users.delete_one({"_id": user_id})
                print("User and related data deleted successfully.")
            else:
                print("Incorrect username")
        else:
            print("Invalid selection.")
    except Exception as e:
        print(f"An error occurred: {e}")


"""def delete_user_data():
    u = users.find({}, {"_id": 0, "user_name": 1})
    users_dict = {}
    for i, doc in enumerate(u, start=1):
        users_dict[i] = doc['user_name']
    for i, p in enumerate(users_dict, start=1):
        print(f'{i}. {users_dict[i]}')
    w = int(input("Select one: "))
    s = users_dict[w]
    user = users.find_one({"user_name": s})
    if user:
        user_id = user["_id"]
        census.delete_one({"_id": user_id})
        users.delete_one({"_id": user_id})
        print("User and related data deleted successfully.")
    else:
        print("Incorrect username")"""

"""c = voting.find({}, {"_id": 0, "party": 1})
party_dict = {}
for i, doc in enumerate(c, start=1):
    party_dict[i] = doc['party']
for i, p in enumerate(party_dict, start=1):
    print(f'{i}. {party_dict[i]}')
w = int(input("Select one: "))
s = party_dict[w]
a = voting.find_one({"party": s})
print(a)"""

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
# x = {"user_name": "Admin2", "password": "2222", "privilege": "admin", "status": "na"}
# users.insert_one(x)
# print(msg)

# n = 1
for x in users.find():
    print(x)
# n += 1
# mycol.find({},{ "_id": 0, "name": 1, "address": 1 })
# candidate = dict(name=input("Candidate name: "), party=input("Represented party: "), gender=input("Gender: "), vote_count=0)
"""c = voting.find({}, {"_id": 0, "party": 1})
for i, c in enumerate(c, start=1):
    print(f"{i}. {c['party']}")"""

# print(x.inserted_id)
