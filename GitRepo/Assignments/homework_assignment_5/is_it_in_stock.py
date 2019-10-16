ab = ("Tacos", "Chips", "Salsa", "Quesadilla")
cd = ("Tacos", "Guacamole", "Burrito", "Chips", "Salsa")


for j in cd: 
    if j in ab:
        print("We have " + str(j).lower() + " in stock.")
    else:
        print("We do not have " + str(j).lower() + " in stock.")
    
    

        




