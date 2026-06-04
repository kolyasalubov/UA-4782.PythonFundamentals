#8.2
def check_password(password):
    has_lower = False
    has_upper = False
    has_numbers = False
    has_special = False
    length_norm = False
    if 6 < len(password) < 16:
        length_norm = True
    for char in password:
        if char.isdigit():
            has_numbers = True
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char in "@#$%&":
            has_special = True
    if has_lower and has_upper and has_numbers and has_special and length_norm:
        print("Valid password")
    else:
        print("Invalid password")

check_password(input("Enter your password: "))
