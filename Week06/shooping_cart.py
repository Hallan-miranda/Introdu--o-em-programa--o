shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

max_price = 0
item_cart = ""

for item in shopping_cart:
    if item[1] > max_price:
        item_cart = item[0]
        max_price = item[1]

print(f"The Maximun price is {max_price} of {item_cart}")