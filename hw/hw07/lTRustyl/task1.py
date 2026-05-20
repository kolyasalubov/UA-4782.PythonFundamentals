def largerThan(first, second):
    """This function takes two numbers and compares them, then tells user which one is bigger."""
    if first > second:
        return print(first, "is bigger than", second)
    elif first < second:
        return print(first, "is less than", second)
    else:
        return print("Those numbers are equal")

largerThan(1,5)
largerThan(10,50)
largerThan(3,2)
largerThan(2**16,5**6)
largerThan(2**2,4)

a = int(input("Write your first number - "))
b = int(input("Write your second number - "))
largerThan(a,b)

print("DocString of the function -", largerThan.__doc__)
