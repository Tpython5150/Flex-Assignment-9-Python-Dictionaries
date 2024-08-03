'''
Restaurant Menu Update 1 task 1
 
You are given an itital structure of a restaurant menu stored in a nested dicitionary. Your task is to update this menu based on given Instructions.

- Add a new category called "Beverages" with at least two items.
- Update the proce of "Steak" to 17.99
- Remove "Bruschetta" from "Starters".

'''

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
    
}

def add_category(menu, category): # Functon adding category to category
    if category not in menu:
        menu[category] = {}   # Dict added for category not already there. 
        print(f"{category} added.")
    else:
        print(f"{category} already exists.")

            
def add_item(menu, category, item): # Function adding item to category in menu
    if category in menu:
        if item not in menu[category]:
            menu[category] =  {}  #Dict added item
            print(f"Item '{item}' added to '{category}'.")
        else:
            print(f"Item '{item}' already exists in '{category}'.")
    else:
        print(f"Category '{category}' does not exist.") 

def add_price(menu, category, item, price):  # Function adding price to item, in category in menu
    if category in menu:
        if price not in menu[category]:
            menu[category][item] = price # Added price to item, in category in menu
            print(f"Price '${price:.2f}' added to '{item}'.")
        else: 
            print(f"Price '{price:.2f} already added to '{item}'.")
    else:
        print(f"Category '{category}' does not exist.")
        
def update_price(menu, category, item, new_price):  # Function dating items price
    if category in menu and item in menu[category]:
        menu[category][item] = new_price  # Update new_price to item to item, in category in menu
        print(f"Item '{item}' in the '{category}' price updated to ${new_price:.2f}.")
    else:
        print(f"Item '{item}' does not exist ")

def remove_item(menu, category, item):  # Function removing item from category, from menu
    if category in menu:
        removed_item = menu[category].pop(item)  # Showing code for item removed
        print(f"Item '{item}' removed from '{category}'.")
    else:
        print(f"Item '{item}' does not exist.")

def display_menu(menu):  # Displaying restaruant menu
    for category, items in menu.items():
        print(f"{category}:")  # Category
        for item, price in items.items():
            if price is not None:
                print(f"  - {item}: ${price:.2f}")  # Item and Price
            else:
                print(f"  -{item}")               

add_category(restaurant_menu, "Beverages")
add_item(restaurant_menu, "Beverages", "Coffee")
add_item(restaurant_menu, "Beverages", "Soda")
add_price(restaurant_menu, "Beverages", "Coffee", 2.25) 
add_price(restaurant_menu, "Beverages", "Soda", 1.50)             
update_price(restaurant_menu, "Main Course", "Steak", 17.99)
remove_item(restaurant_menu, "Starters", "Bruschetta")
display_menu(restaurant_menu)