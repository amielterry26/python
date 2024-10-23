# Notes:
# Age app to get in the club. If they are younger than 19, they are too young.
# If they are between 19 - 55, they are welcome in.
# If they are older than 55, they are too old.
# a secondary if statement is written with "elif"

age = int(input("How old are you? "))

print(f"So you are {age}.")

# Logic

if age < 19:
    print("You are too young.")
elif age > 55:
    print("You are too old.")
else:
    print("Congrats, welcome in!")
