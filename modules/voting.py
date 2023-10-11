# Election

from modules.functions import create, update


def voting(user_id, privilege):
    print("Election Time")
    print("You must be logged in as a user to vote")
    while True:
        if privilege == "user":
            _do = eval(input("What would you like to do?\n1: Vote\n2: View results\n3: Exit: "))
            if _do == 1:
                pass  # increase vote_count function
            elif _do == 2:
                pass  # fetch details
            elif _do == 3:
                break
            else:
                print("Invalid option. Type either \"1\", \"2\" or \"3\"")
        elif privilege == "admin":
            _do = eval(input("What would you like to do?\n1: Add new Candidate\n2: Update candidate details\n3: Delete Candidate\n4: Exit: "))
            if _do == 1:
                candidate = dict(name=input("Candidate name: "), party=input("Represented party: "),
                                 gender=input("Gender: "), vote_count=0)
                create(candidate, msg="Candidate added successfully", db="voting")
            elif _do == 2:
                update(_id=user_id, msg="Details edited Successfully", db="voting")
            elif _do == 3:
                pass  # delete function
            elif _do == 4:
                break
            else:
                print("Invalid option. Type either \"1\", \"2\" or \"3\"")
