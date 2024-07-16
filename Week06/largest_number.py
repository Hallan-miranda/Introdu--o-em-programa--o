numbers = [20, 30, 37, 15, 22, 87, 90]

largest = 0

for number in numbers :
    if largest < number:
        largest = number
    
print(f"The largest number is: {largest}")