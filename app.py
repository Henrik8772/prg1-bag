bag = True
inventory = []
print("Welcome to your inventory!")

while bag:

    print("Show items [I]")
    print("Save in the bag [S]")
    print("End program [E]")
    choice = input("Choose: ")

    if choice.lower() == "i":
        for thing in inventory:
            print(thing)

    elif choice.lower() == "s":
        inventory.append(input("Write what you want to save: "))

    elif choice.lower() == "e":
        bag = False

    else:
        print("Error unknown command, try again.")
