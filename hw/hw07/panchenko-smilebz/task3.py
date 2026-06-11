def count_characters(text):
    """
    Counts the occurrences of each character in the given text.

    Parameters:
    text (str): The text to analyze.

    Returns:
    dict: A dictionary with characters as keys and their counts as values.
    """
    result = {}

    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


word = input("Enter a word: ")
print(f"Character counts for '{word}': {count_characters(word)}")
