first = input("What's your first name? ")
middle = input("What's your middle name? ")
last = input("What's your last name? ")

if middle == "":
    print(first, last)
else:
    print(first, middle, last)

