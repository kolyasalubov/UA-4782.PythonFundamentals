###homework task 1

from typing import Tuple
def bigger_numbers(x: float ,y: float):
    """
    this function will help determine which number is larger
    x - first number
    y - second number
    """

    if  x > y :
     return x
    else :
     return y

x = float(input("enter sum1 :"))
y = float(input("enter sum2 :"))

result = bigger_numbers(x, y)
print(f"the larger number is ", {result})



###homework task 2

import math

def rectangle(a: float, b: float) -> float:
    """Обчислює площу прямокутника"""
    return a * b

def triangle(base: float, height: float) -> float:
    """Обчислює площу трикутника за основою та висотою"""
    return 0.5 * base * height

def circle(radius: float) -> float:
    """Обчислює площу кола за радіусом"""
    return math.pi * (radius ** 2)


print("Оберіть фігуру:")
print("1 - Прямокутник")
print("2 - Трикутник")
print("3 - Коло")

choice = input("Ваш вибір (1/2/3): ")

if choice == "1":
    w = float(input("Введіть ширину: "))
    h = float(input("Введіть висоту: "))
    print(f"Площа прямокутника: {rectangle(w, h):.2f}")

elif choice == "2":
    b = float(input("Введіть основу трикутника: "))
    h = float(input("Введіть висоту трикутника: "))
    print(f"Площа трикутника: {triangle(b, h):.2f}")

elif choice == "3":
    r = float(input("Введіть радіус кола: "))
    print(f"Площа кола: {circle(r):.2f}")

else:
    print("Неправильний вибір!")


###homework task 3

from collections import Counter

def my_count(text):
    return dict(Counter(text))

user_input = "hello"
print(my_count(user_input))






##homework 3 Practical task

##I. Jenny's secret message

def greet(name: str) -> str:
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

print(greet("Anna"))   
print(greet("Johnny"))

##II. Find The Distance Between Two Points

import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)

point_A = (1, 2)
point_B = (4, 6)

result = calculate_distance(point_A, point_B)
print(f"Відстань між точками: {result}")



##III. No yelling!

text="HELLO CAN YOU HEAR ME"
text2="now THIS is REALLY interesting"
text3="THAT was EXTRAORDINARY!"

print(text.capitalize())
print(text2.capitalize())
print(text3.capitalize())

###IV. Convert a Number to a String
number1 = 123
print(f"'{number1}'")

number2 = 999
print(f"'{number2}'")

number3 = -100
print(f"'{number3}'")


number = 555
result = f"'{number}'"





##V. Reversing Words in a String


def reverse_words(text):
    words = text.split()
    return " ".join(words[::-1])

print(reverse_words("Hello World"))  
print(reverse_words("Hi There."))
print(reverse_words("       Hi      There."))  



###VI. Reverse List Order


def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1, 2, 3, 4]))  
print(reverse_list([9, 2, 0, 7]))


###VII. Multiples of 3 or 5

def solution(number):
    if number < 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)


print(solution(12))  
print(solution(-7))


##VIII. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    return max_distance >= distance_to_pump


print(zero_fuel(50, 25, 2))  
print(zero_fuel(75, 25, 2))


##IX. Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


print(are_you_playing_banjo("Roman"))  
print(are_you_playing_banjo("regina")) 
print(are_you_playing_banjo("Olexandr")) 


##X. Convert boolean values to strings 'Yes' or 'No’

def bool_word(boolean):
    return "Yes" if boolean else "No"


print(bool_word(True))
print(bool_word(False)) 


##XI. Counting sheep

def count_sheeps(sheep_list):
    return sheep_list.count(True)

my_list = [
  True,  True,  True,  False,
  True,  True,  True,  True,
  True,  False, True,  False,
  True,  False, False, True,
  True,  True,  True,  True,
  False, False, True,  True
]

print(count_sheeps(my_list)) 


##XII. Is this my tail?

def correct_tail(body, tail):
    return body.endswith(tail)

print(correct_tail("Fox", "x"))       
print(correct_tail("Rhino", "o"))     
print(correct_tail("Meerkat", "t"))   
print(correct_tail("Emu", "a")) 
print(correct_tail("Badger", "s"))
print(correct_tail("Giraffe", "d"))