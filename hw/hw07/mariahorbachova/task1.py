def get_thelargest(num1, num2):
    """
    This function compares two numbers and return the larger one.
    """
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Numbers are equel."

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))    

result = get_thelargest(num1, num2)
print("Result:", result)