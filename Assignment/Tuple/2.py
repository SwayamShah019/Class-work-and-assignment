#Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price.
menu=[("Pizza", 450), ("Burger", 200), ("Lava Cake", 150), ("Oreo Shake", 175)]
price=[]
new_menu=[]
for i in menu:
    price.append(i[1])
while len(menu)>0:
    new_menu.append(menu[price.index(max(price))])
    menu.pop(price.index(max(price)))
    price.remove(max(price))
print(new_menu)
