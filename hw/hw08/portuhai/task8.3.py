import module83
type_fig = input("Area of which figure are you trying to get? ").lower()

if type_fig == "circle":
    r = float(input("Radius of circle: "))
    print(round(module83.circle_area(r), 4))

elif type_fig == "rectangle":
    a, b = map(float, input("Sides of rectangle (separated by space): ").split())
    print(round(module83.rectangle_area(a, b), 4))

elif type_fig == "triangle":
    a, h = map(float, input("Side and height of triangle (separated by space): ").split())
    print(round(module83.triangle_area(a, h), 4))

else:
    print("Unknown figure type!")