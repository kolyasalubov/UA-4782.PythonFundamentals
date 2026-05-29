def max_number(a, b):
    """
    Returns the largest of two numbers.

    Parameters:
    a (int or float): first number
    b (int or float): second number

    Returns:
    int or float: largest number
    """
    return a if a > b else b


a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print(max_number(a, b))
