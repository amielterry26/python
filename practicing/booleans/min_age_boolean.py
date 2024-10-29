# Define the minimum age requirement
minimum_age = 21

# Ask the user for their age
age = int(input("Please enter your age: "))

# Check if the user meets the age requirement
if age >= minimum_age:
    is_allowed_access = True
else:
    is_allowed_access = False

# Use the Boolean variable in an if statement
if is_allowed_access:
    print("Access granted! Welcome to the restricted section.")
else:
    print("Access denied. You must be at least 21 years old.")