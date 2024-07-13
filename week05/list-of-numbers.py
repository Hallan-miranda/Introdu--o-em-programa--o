numbers = []
sum = 0
average = 0
largest = 0
smallest = 10000
quantit = 0

print("Enter a list of numbers, type 0 when finished.")
number = int(input("Enter the number: "))

while number != 0:
    if number > largest:
        largest = number
    else:
        largest = largest

    if number > 0 and number < smallest:
        smallest = number
    else:
        smallest = smallest

    if number != 0:
        quantit = quantit + 1
        sum = sum + number
        numbers.append(number)
        number = int(input("Enter the number: "))
print(f"The sum is: {sum}" )
print(f"The average is: {average}" )
print(f"The largest number is: {largest}")
print(f"The smallest positive number is: {smallest}")
print("The sorted list is:")
for number in numbers:
    print(number)
