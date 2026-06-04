#7.3.1
def greet(name: str):
    if name == "Johny":
        print("Hiiii, Johny)")
    else:
        print("Hello, " + name)
#7.3.2
def calculate_distance(p1: tuple, p2: tuple) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)
#7.3.3
def clean_and_capitalize(text: str) -> str:
    return " ".join(text.split()).capitalize()
#7.3.4
def int_to_str(numb):
    return str(numb)
#7.3.5
def reverse_phrase(phrase: str):
    first = 0
    second = 0
    for c in range(len(phrase)):
        if phrase[c] == " ":
            first = phrase[0:c]
            second = phrase[c:]
    return second + " " + first
#7.3.6
def reverse(lst):
    return lst[-1::-1]
#7.3.7
def sum_of_multipliers35_under(number):
    summ = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            summ += i
    return summ
#7.3.8
def fuel_counter(distance: int or float, fuel: int or float, distance_per_gallon):
    if fuel * distance_per_gallon >= distance:
        return True
    else:
        return False
#7.3.9
def play_banjo(name: str):
    if name[0] == "R" or name[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
#7.3.10
def yes_no(value: bool):
    if value:
        return "Yes"
    else:
        return "No"
#7.3.11
def count_sheep(sheep):
    count = 0
    if sheep is list:
        for i in sheep:
            if i == True:
                count += 1
    else:
        print("Enter a normal list")
    return count

#7.3.12
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False
