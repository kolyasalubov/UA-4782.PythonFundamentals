#7.1.1
def bigger(x: int or float, y: int or float):
    """
    A function that returns a bigger number out of two
    x: int or float
    y: int or float
    """
    if x > y:
        return x
    else:
        return y

#7.1.2
import math

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 1/2

def circle_area(radius):
    return math.pi * radius ** 2

def rectangle_area(width, height):
    return width * height

def main():
    print(f"The area of a triangle with sides 3, 4, 5 is: {triangle_area(3, 4, 5)}")
    print(f"The area of a circle with radius 7 is: {circle_area(7)}")
    print(f"The area of a rectangle with sides 8, 10 is: {rectangle_area(8, 10)}")
#7.1.3
def char_count(word: str):
    dct = {}
    for i in range(len(word)):
        count = 0
        for n in range(i, len(word)):
            if word[i] == word[n]:
                count += 1

        already_counted = False
        for s in range(0, i):
            if word[s] == word[i]:
                already_counted = True
                break

        if not already_counted:
            dct[word[i]] = count

    return dct
