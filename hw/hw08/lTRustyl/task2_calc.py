from math import pi, pow

def area_of_rectangle(w, l):
    return w*l
    
def area_of_circle(r):
    return pi * pow(r, 2)

def area_of_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return None

    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
