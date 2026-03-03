import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
print("You have 7 attempts to guess the number.")

number = random.randint(1, 100)
attempts = 0
max_attempts = 7

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it.")
        print("Number of attempts:", attempts)
        break
else:
    print("\nGame Over! You've used all your attempts.")
    print("The correct number was:", number)
