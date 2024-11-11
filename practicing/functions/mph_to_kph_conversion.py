def kph(speed):
    result = speed * 1.609
    print(f"You were going {result} kph.")


def mph(speed):
    result = speed // 1.609
    print(f"You were going {result} mph.")


def main():
    while True:
        speed = int(input("How fast were you going? "))
        ph = input("mph or kph? ")
        error = "please input mph or kph, and run script again."

        if ph == "mph":
            kph(speed)
        elif ph == "kph":
            mph(speed)
        else:
            print(error)

        answer = input("Would you like to make another calculation?")
        if answer == "y":
            main()
        else:
            break


main()
