import re

bag = True
inventory = []
print("Welcome to your inventory!🎒\n")


def add_item_from_text(raw_text):
    m = re.match(r"^\s*(\d+)\s*(?:x)?\s*(.+)$", raw_text, re.I)
    if m:
        qty = int(m.group(1))
        name = m.group(2).strip().lower()
        if qty > 0:
            inventory.extend([name] * qty)
    else:
        name = raw_text.strip().lower()
        if name:
            inventory.append(name)


while bag:

    print("Show items [I]")
    print("Save in the bag [S]")
    print("End program [E]")
    print("Search items [F]")
    print("Remove from bag [R] \n")
    choice = input("Choose: ")

    if choice.lower() == "i":
        if inventory:
            print("This is your inventory!😃")
            for thing in sorted(set(inventory)):
                print(f"{inventory.count(thing)}x {thing}")

        else:
            print("Your bag is empty!😭")

    elif choice.lower() == "s":
        items = input(
            "Write what you want to save (seperate them with commas): ")
        new_items = [item.strip() for item in items.split(",") if item.strip()]
        for raw in new_items:
            add_item_from_text(raw)

    elif choice.lower() == "r":
        if not inventory:
            print("Your bag is empty!")
        else:
            print("These are all the items.")
            for thing in sorted(set(inventory)):
                print(f"{inventory.count(thing)}x {thing}")
            to_remove = input(
                "Write what you want to remove (e.g. 'stone' or '2x stone'): ")
            m = re.match(r"^\s*(\d+)\s*(?:x)?\s*(.+)$", to_remove, re.I)
            if m:
                qty = int(m.group(1))
                name = m.group(2).strip().lower()
                removed = 0
                for _ in range(qty):
                    try:
                        inventory.remove(name)
                        removed += 1
                    except ValueError:
                        break
                print(f"Removed {removed}x {name}")
            else:
                name = to_remove.strip().lower()
                try:
                    inventory.remove(name)
                    print(f"Removed 1x {name}")
                except ValueError:
                    print(f"{name} not in inventory")

    elif choice.lower() == "e":
        bag = False

    elif choice.lower() == "f":
        queries = input(
            "What do you want to search for? (seperate with commas): ")
        search_items = [q.strip().lower()
                        for q in queries.split(",") if q.strip()]

        for item in search_items:
            count = inventory.count(item)
            if count > 0:
                print(f"Found: {count}x {item} in your inventory")
            else:
                print(f"{item} not found in your inventory")

    else:
        print("Error unknown command, try again.")
