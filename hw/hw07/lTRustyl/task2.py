from math import pi

def areaOfRectangle(w, l):
    return w*l
    
def areaOfCircle(r):
    return pi*r**2

def areaOfTriangle(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

answer = False

while answer == False:
    answer = input("Hi, if you would like to calculate the area of a triangle, rectangle or circle just write its name - ")
    answer = answer.lower()

    if answer == 'triangle':
        x = float(input('Enter the first side length of your triangle - '))
        y = float(input('Enter the second side length of your triangle - '))
        z = float(input('Enter the third side length of your triangle - '))

        print("The area of your triangle is", areaOfTriangle(x,y,z))
    
    elif answer == 'rectangle':
        width = float(input('Enter the length of your rectangle - '))
        length = float(input('Enter the width of your rectangle - '))

        print("The area of your rectangle is", areaOfRectangle(width, length))

    elif answer == 'circle':
        radius = float(input('Enter the radius of your circle - '))
    
        print("The area of your circle is", areaOfCircle(radius))
    else:
        print("It seems you have entered some other figure, try again!" + '\n')
        answer = False
