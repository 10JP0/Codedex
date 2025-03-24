import math

options = ["Square", "Rectangle", "Triangle", "Circle"]

def welcome():
    print("Hello! This is a area calculator")
    print("Choose wich shape do you want to discover the are:\n1 - Square\n2 - Rectangle\n3 - Triangle\n4 - Circle\n5 - Quit")
    while True:
        try:
            answer = int(input("Which shape have you chosen: "))
            if 1 <= answer <= 5:
                if answer == 5:
                    print("Good bye, have a good day.\nCome back when you need to calculate some areas!")
                    quit()
                break
            else:
                print("Sorry, something went wrong. Choose the shape again.\n")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.\n")
    return answer

def check_shape(shape):
    print(f"\nLet's calculate the area of a {options[shape - 1]}!\n")
    if shape == 1:
        area = square()
    elif shape == 2:
        area = rectangle()
    elif shape == 3:
        area = triangle()
    elif shape == 4:
        area = circle()
    print(f"The area of {options[shape - 1]} is equal to {area}")

def square():
    side = float(input("Enter the side length: "))
    return side ** 2

def rectangle():
    side1 = float(input("Enter the side length: "))
    side2 = float(input("Enter the side width: "))
    return side1 * side2

def triangle():
    height = float(input("Enter the height: "))
    base = float(input("Enter the base: "))
    return (height * base) /2

def circle():
    pi = math.pi
    radius = float(input("Enter the radius: "))
    return pi * (radius ** 2)





shape = welcome()

check_shape(shape)








