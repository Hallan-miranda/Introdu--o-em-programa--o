# In this game you must introduce the corresponding options if it does not return an error
# Option must be entered as INT name with STR and values ​​with FLOAT
name_item = []
price_item = []
cart = []
shooping_cart_item = 0
repeat = True
item_quantit = 0
index = 0
remove_item = 0
total = 0

print("Welcome to the Shopping Cart Program!")
while repeat == True:
    print(":Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit\n")

    action = int(input("Please enter an action: "))

    if action == 1:  
        item = input("What item would you like to add? ")
        value = float(input(f"What is the price of '{item}'? "))
        name_item.append(item)
        price_item.append(value)
        shooping_cart_item = shooping_cart_item + 1
        print(f" {item}has been added to the cart.\n")
    elif action == 2:
        print("The contents of the shopping cart are:")
        item_quantit = 0
        index = 0
        for item in name_item:
            item_quantit = item_quantit + 1
            print(f"{item_quantit}. {name_item[index]} - ${price_item[index]:.2f}")
            index = index + 1
    elif action == 3:
        print("\nThe contents of the shopping cart are:")
        item_quantit = 0
        index = 0
        for item in name_item:
            item_quantit = item_quantit + 1
            print(f"{item_quantit}. {name_item[index]} - ${price_item[index]:.2f}")
            index = index + 1
        remove_item = int(input("Which item would you like to remove? "))
        if remove_item <= item_quantit and remove_item > 0:
            del name_item[remove_item - 1]
            del price_item[remove_item - 1]
        elif item_quantit == 0:
            print("Sorry, don't have any item on the cart")
        else:
            print("Sorry, that is not a valid item number.\n")
    elif action == 4:
        total = 0
        for price in price_item:
            total = total + price
        print(f"The total price of the items in the shopping cart is {total:.2f} \n")
    elif action == 5:
        repeat = False
        print("Thank you. Goodbye.")