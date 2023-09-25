x = {}
msg = "Success"


def edit(x, msg):
    while True:
        print(x)
        print("What would you like to edit\nType \"exit\" if you made a mistake or changed your mind")
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
                x[option] = new
                print(msg)
                break
            except KeyError:
                print("Invalid option")


def create(x, msg):
    while True:
        print(x)
        really = input("Is this correct? (Y/N): ")
        if really == "Y".lower():
            print(msg)
            break
        elif really == "N".lower():
            edit(x, msg="Details edited Successfully")
        else:
            print("Invalid option")
