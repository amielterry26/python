# Problem Statement:
# Make an age entry app using functions. (3)
# print output based on user input

# Functions
def too_young(age):
    print("You are too young to enter.")

def too_old(age):
    print("you are too old.")


# Variables
age = int(input("How old are you? "))
legal_age = 18

# Script/logic
if age < legal_age:
    too_young(age)
elif age > legal_age + 47:
    too_old(age)
else:
    print("you may enter!")
