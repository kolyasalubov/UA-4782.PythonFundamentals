import math

def rectangle(a, b):
    return a * b

def triangle(a, h):
    return 1/2 * a * h 

def circle(r):
    return math.pi * r**2


option = int(input("1 - Rectangle \n2 - Triangle \n3 - Circle \nSelect an option: "))

if option == 1:
    a = float(input("Enter the first side (a): "))
    b = float(input("Enter the second side (b): "))
    result = rectangle(a, b)
    print("The area of ​​a rectangle:", round(result, 2))

elif option == 2:
    a = float(input("Enter the base (a): "))
    h = float(input("Enter the height (h): "))
    result = triangle(a, h)
    print("The area of ​​a triangle:", round(result, 2))

elif option == 3:
    r = float(input("Enter the radius (r): "))
    result = circle(r)
    print("The area of ​​a circle:", round(result, 2))

else:
    print("Wrong option number.")
