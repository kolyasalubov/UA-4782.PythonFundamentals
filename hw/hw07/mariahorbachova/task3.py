

def calculate_characters(input_string):
    char_count = {}

    for i in input_string:
        if i not in char_count:
            char_count[i] = 1
        else:
            char_count[i] += 1

    return char_count

input_string = input("Enter your string: ")
print(calculate_characters(input_string))