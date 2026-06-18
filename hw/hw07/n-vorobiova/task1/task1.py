def get_largest_number(num1, num2):
    """
    Parameters:
    num1: The first number.
    num2: The second number.
    
    Returns:
    The larger number.
    """
    if num1 > num2:
        return num1
    else:
        return num2

number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))

# Виклик функції та вивід результату
result = get_largest_number(number1, number2)
print(f"The largest number is: {result}")