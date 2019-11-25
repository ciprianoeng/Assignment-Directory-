
#menu_dictionary
menu = {
    "Chicken" : 10 ,
    "Beef" : 15 ,
    "Salmon" : 20 ,
    "Mashed Potatoes" : 5 ,
    "Rice" : 7 ,
    }

#customer_order
customer_order = ("Chicken", "Pork", "Mashed Potatoes")

#for_loop1
for item in customer_order:
    if item in menu:
        print(item + ": $" + str(menu[item]))
    else:
        print("We do not have " + item)
print("-----------")
print("Order Total: $15")
        

