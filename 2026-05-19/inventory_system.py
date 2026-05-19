inventory = {
    "Rice": 60.00,
    "Sugar": 45.50,
    "Milk": 30.00,
    "Apple": 72.00,
    "Bread": 40.00,
    "Salt": 25.60,
    "Orange": 50.00,
    "Butter": 20.00,
    "Cheese": 15.00,
    "Curd": 25.00,
    "Coffee Powder": 35.00,
    "Grapes": 40.50
    }

cart = ["Sugar", "Milk", "Coffee Powder","Cooking Oil"]
 
 #Types of variables in Inventory System
print("Inventory System Variable Types:")
print(f"Inventory: {type(inventory)}")
print(f"Price of Rice: {type(inventory['Rice'])}")
print(f"Cart: {type(cart)}")

#Calculate Total Bill
print("\Total Bill:")
total_bill = 0
for item in cart:
    if item in inventory:
        total_bill += inventory[item]       
print(f"Total Bill: {total_bill}")

#Item Availability
print("\nItem Availability:")
for item in cart:
    if item in inventory:
        print(f"{item} is available at price {inventory[item]}")
    else:
        print(f"{item} is NOT AVAILABLE in the inventory.")


cart = set(cart)
print("\nCart as a Set:", cart)

#Product Categories
product_categories = ("Grocery", "Dairy", "Fruits")
print("\nProduct Categories:") 
for i in product_categories : 
    print(i, type(i))

inventory["Coconut"] = None
print("Type of Coconut price:", type(inventory["Coconut"]))

is_discounted = total_bill > 100


print("\n============Purchase Details: ==============")
print("Items Purchased:\n")
for item in cart:
    if item in inventory:
        print(f"{item}: {inventory[item]}")
print(f"\nTotal Bill: {total_bill}")  
print("\nIs Discounted:", is_discounted)