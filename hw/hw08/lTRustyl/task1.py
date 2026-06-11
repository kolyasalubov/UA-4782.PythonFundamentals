import re

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{6,16}$'

while True:
    password = input('Enter your password - ')

    if re.match(pattern, password):
        print("Valid password.")
        break
    else:
        print("Invalid password, try again.")
