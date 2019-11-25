#Carlos Cipriano
#019076
#11/03/19
#MSITM 6341

menu_items = {}

should_ask_for_item = True

while should_ask_for_item:

    item = input("Item Name: ")
    cost = input("Item Cost: ")

    if item in menu_items:
        print("WARNING: Item exists")

    menu_items[item] = cost

    continue_or_not = input("Continue(Y/N)? ")

    if continue_or_not == "N":
        should_ask_for_item = False

for item, cost in menu_items.items():
    print("Item Name: " + item + " Cost: " + cost)
