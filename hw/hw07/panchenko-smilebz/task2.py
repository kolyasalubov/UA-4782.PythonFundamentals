from math import pi


def rectangle_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width


def triangle_area(base, height):
    """Calculates the area of a triangle."""
    return 0.5 * base * height


def circle_area(radius):
    """Calculates the area of a circle."""
    return pi * radius**2


choice = input("Choose shape (rectangle, triangle, circle): ").lower()

if choice == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area:", rectangle_area(length, width))

elif choice == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area:", triangle_area(base, height))

elif choice == "circle":
    radius = float(input("Enter radius: "))
    print("Area:", round(circle_area(radius), 2))

else:
    print("Invalid choice")
