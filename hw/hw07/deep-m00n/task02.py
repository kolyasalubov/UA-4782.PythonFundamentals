PI = 3.14

def rectangle_area(a, b):
    return a * b

def triangle_area(base, height):
    return base * height / 2

def circle_area(r):
    return PI * r * r

print("Calculate the area of a\n")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle\n")

choice = int(input("Choose an option (1-3): "))
print()

area = None

if choice == 1:
    a = float(input("a = "))
    b = float(input("b = "))
    area = rectangle_area(a, b)

elif choice == 2:
    base = float(input("base = "))
    height = float(input("height = "))
    area = triangle_area(base, height)

elif choice == 3:
    r = float(input("r = "))
    area = circle_area(r)

else:
    print("Invalid choice.")

if area is not None:
    print(f"\nArea = {area}")
