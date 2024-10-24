# The purpose of a function has 3 layers.
# The first layer is to name the function and it's components. - (The name)
# The second layer is to define how the function does it. - (The Logic)
# The third layer is to determine what you want the functino to do when called. - (The Output)

# Practice Example:
# My attempt:
def remainder(x, y):
    result = (x % y)
    print(result)


x = int(input("How many seats are available? "))
y = int(input("How many people in your party? "))

remainder(x, y)

# Correct attempt:

def remainder(a, b):
    result = (a % b)
    print(result)

seats_available = int(input("How many seats are available? "))
party_size = int(input("How many people in your party? "))

remainder(seats_available, party_size)