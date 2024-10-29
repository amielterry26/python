# This is going to be an example .py file for boolean practice.
# Ask the user for their credentials

# Simulate correct credentials
correct_username = "admin"
correct_password = "password123"

username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

# Check if the credentials are correct
if username == correct_username and password == correct_password:
    is_logged_in = True
else:
    is_logged_in = False

# Use the Boolean variable in an if statement
if is_logged_in:
    print("Welcome back!")
else:
    print("Invalid credentials, please try again.")

