#1
def process_age(age_str):
    age = int(age_str)
    if age < 0:
        raise ValueError("Age cannot be a negative number!")
    if age % 2 == 0:
        return f"The age {age} is even."
    else:
        return f"The age {age} is odd."

#2
def get_day_of_week(number_str):
    try:
        num = int(number_str)
        days = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
        if num in days:
            return f"Day {num} is {days[num]}."
        elif num >= 8 or num <= 0:
            return f"Error: There is no day with number {num} in a week (must be 1-7)."
        else:
            return None

    except ValueError:
        return "Error: Invalid input! You must enter a number."


user_input = input("Enter your age: ")
try:
    result = process_age(user_input)
    print(result)
except ValueError as e:
    print(f"Exception caught: {e}")
user_day = input("Enter a number (1-7) to get the day of the week: ")
print(get_day_of_week(user_day))