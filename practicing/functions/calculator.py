# This is going to be a calculator function.

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


x = int(input("what is x? "))
y = int(input("what is y? "))

add(x, y)
sub(x, y)
div(x, y)
multiply(x, y)
mean(x, y)
