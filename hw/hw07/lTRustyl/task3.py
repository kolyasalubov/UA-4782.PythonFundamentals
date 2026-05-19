def characterCalculator(input):
    input = input.lower()
    output = {}
    
    for i in range(len(input)):
        count = 0
        for j in range(len(input)):
            if input[i] == input[j]:
                count += 1
        output.update({input[i]: count})

    return print("The number of letters in your word -", output)

word = input("Write a word - ")
characterCalculator(word)
