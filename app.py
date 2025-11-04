bag = True
inventory = []
print("Welcome to your inventory!🎒\n")

while bag:

    print("Show items [I]")
    print("Save in the bag [S]")
    print("End program [E]")
    print("Remove from bag [R] \n")
    choice = input("Choose: ")

    if choice.lower() == "i":
        if inventory:
            print("This is your inventory!😃")
            for thing in inventory:
                print(thing)
        else:
            print("Your bag is empty!😭")

    elif choice.lower() == "s":
        items = input(
            "Write what you want to save (seperate them with commas): ")
        new_items = [item.strip() for item in items.split(",")]
        inventory.extend(new_items)

    elif choice.lower() == "r":
        print("These are all the items.")
        for thing in inventory:
            print(thing)
        inventory.remove(input("Write what you want to remove: "))

    elif choice.lower() == "e":
        bag = False

    else:
        print("Error unknown command, try again.")
