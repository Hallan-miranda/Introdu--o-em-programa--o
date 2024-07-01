#the calculator meal price recive a sertains values of price amount and tax to calculate the total for payed.

price_childre_meal = float(input("What is the price of a child's meal? "))
price_adults_meal = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))
total= price_childre_meal * number_of_children + number_of_adults * price_adults_meal
print(f"\n Subtotal: ${total:.2f}\n")
sales_tax = float(input("What is the sales tax rate? "))
sales_tax_rate = (total / 100) * int(sales_tax)
total_with_tax = sales_tax_rate + total
print(f"Sales tax: {sales_tax_rate}")
print(f"total {total_with_tax}")
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total_with_tax
print(f"Change: {change:.2f}")