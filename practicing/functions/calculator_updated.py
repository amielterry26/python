# This is going to be a calculator function.

# FUNCTIONS
def add(x, y):
    result = x + y
    print(result)


def sub(x, y):
    result = x - y
    print(result)


def div(x, y):
    result = x/y
    print(result)


def multiply(x, y):
    result = x*y
    print(result)


def mean(x, y):
    result = x+y / 2
    print(f"This is the mean of your two integers {result}")


# VARIABLES
x = int(input("what is x? "))
y = int(input("what is y? "))
answer = int(input("What operation? "))
error = "Please input a number between 1-5 and run script again."

# Actual script ↓
if answer == 1:
    add(x, y)
elif answer == 2:
    sub(x, y)
elif answer == 3:
    div(x, y)
elif answer == 4:
    multiply(x, y)
elif answer == 5:
    mean(x, y)
else:
    print(error)

