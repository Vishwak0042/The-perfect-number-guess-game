import random

number_to_guess = random.randint(1, 100)
guess = None
attempts = 0

while guess != number_to_guess:
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1

    if guess > number_to_guess:
        print("Lower number please")
    elif guess < number_to_guess:
        print("Higher number please")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")

