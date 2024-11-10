def kph(speed):
    result = speed * 1.609
    print(f"You were going {result} kph.")


def mph(speed):
    result = speed // 1.609
    print(f"You were going {result} mph.")


speed = int(input("How fast were you going? "))
ph = input("mph or kph? ")
error = "please input mph or kph, and run script again."

if ph == "mph":
    kph(speed)
elif ph == "kph":
    mph(speed)
else:
    print(error)

