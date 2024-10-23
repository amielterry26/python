import random

user_guess = input("What time is it?\n")

print(f"Your guess was {user_guess}.")

answer = random.randint(1, 12)

if user_guess == answer:
    print("You got it right!")
else:
    print(f"Nope,The answer was {answer}.")
