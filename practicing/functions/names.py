# This function will get a name input and call the function to give a salutation to that name.
def salutation(name):
    print(f"Welcome to Avalon, {name.capitalize()}!")


def main():
    name = str(input("what is your name? "))
    salutation(name)


main()
