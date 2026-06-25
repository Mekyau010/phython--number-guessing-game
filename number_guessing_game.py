import random

print("=== Welcome to Aminu Bashir's Number Guessing Game ===")

secret = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")
