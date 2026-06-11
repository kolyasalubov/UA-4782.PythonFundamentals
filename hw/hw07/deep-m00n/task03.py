def count_characters(text: str) -> dict:
    chars = {}

    for char in text:
        chars[char] = chars.get(char, 0) + 1

    return chars

print(count_characters("hello"))
