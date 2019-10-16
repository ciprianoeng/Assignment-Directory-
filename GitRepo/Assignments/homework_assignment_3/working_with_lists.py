grocery_store_items = ['Apple', 'Orange', 'Steak', 'Chicken', 'Water']
grocery_item_price = ['10', '20', '30', '40', '50']

#1. 
print(grocery_store_items[2], grocery_item_price[2])
#2.
print(grocery_store_items[-1], grocery_item_price[-1])
#3.
grocery_store_items.insert(5, 'Paneapple')
grocery_item_price.insert(5, '60')
#4.
print(grocery_store_items)
#5.
print(grocery_item_price)
#6.
del grocery_store_items[0]
del grocery_item_price[0]
#7.
for i in grocery_item_price:
    grocery_item_price.insert(1, i*2)  
#8.
print(grocery_store_items)
#9.
print(grocery_item_price)