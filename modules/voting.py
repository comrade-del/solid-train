# Election

from modules.functions import create


def voting(user_id, privilege):
    print("Election Time")
    candidate = dict(name=input("Candidate name: "), party=input("Represented party: "),
                     gender=input("Gender: "), vote_count=0)

    create(candidate, msg="Candidate added successfully")
    # turn into if else for adding candidates and voting or make into functions
