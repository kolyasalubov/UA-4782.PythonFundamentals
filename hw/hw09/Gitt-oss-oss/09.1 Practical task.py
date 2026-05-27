from random import randint

secret_number = randint(1, 100)

attempts = 10

print("Welcome to the Guess the Number game!")
print("You have 10 attempts to guess a number from 1 to 100.")

for attempt in range(1, attempts + 1):
    guess = int(input(f"\nAttempt {attempt}: Enter your number: "))

    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("The secret number is greater.")
    else:
        print("The secret number is smaller.")

else:
    print(f"\nYou lost! The secret number was {secret_number}.")