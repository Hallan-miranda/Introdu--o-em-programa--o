import math

length_side_square = float(input("What is the length of a side of the square? "))
area_of_square = length_side_square * length_side_square
print(f"The area of the square is: {area_of_square:.2f}")
length_retangle = float(input("What is the length of rectangle? "))
Width_retangle = float(input("What is the width of the rectangle? "))
area_retangle = length_retangle * Width_retangle
print(f"The area of the rectangle is: {area_retangle:.2f}")
radius_circle = float(input("What is the radius of the circle? "))
circle_area = math.pi * radius_circle **2
print(f"The area of the circle is: {circle_area:.4f}")
