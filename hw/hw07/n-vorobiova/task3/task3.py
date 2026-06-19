def count_characters(text):
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

user_input = "hello"
output = count_characters(user_input)
print(output)