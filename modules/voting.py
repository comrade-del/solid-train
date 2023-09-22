# Election

from modules.functions import create

print("Election Time")

candidate = dict(name=input("Candidate name: "), party=input("Represented party: "),
                 gender=input("Gender: "), vote_count=0)

create(candidate, msg="Candidate added successfully")
