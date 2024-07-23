import math
reapet = True

def compute_area_square(square_site):
    square_area = square_site * square_site
    return square_area

def compute_area_rectangle(rectangle_width, rectangle_heigth):
    rectangle_area = rectangle_width * rectangle_heigth
    return rectangle_area

def compute_area_circle(radius_circle):
    circle_area = math.pi * (radius_circle * radius_circle)
    return circle_area

while reapet == True:
    shape = input("what kind of shape you have a CIRCLE, a SQUARE or a RECTANGLE? ").lower()
    if shape == "square":
        square_side = float(input("what's your square side? "))
        print(round(compute_area_square(square_side)))
    elif shape == "rectangle":
        rectangle_heigth = float(input("what's your rectangle heigth? "))
        rectangle_width = float(input("what's your rectangle width? "))
        print(round(compute_area_rectangle(rectangle_width, rectangle_heigth)))
    elif shape == "circle":
        radius_circle = float(input("What is the radios do the circle? "))
        print(round(compute_area_circle(radius_circle), 2))
    else:
        reapet = False