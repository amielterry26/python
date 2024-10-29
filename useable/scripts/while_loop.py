i = 0

while i < 9:
    print("Incorrect. ")
    print(i)
    i = i + 1

    if i == 4:
        print("You've been locked out.")
        print("You will now be redirected to the homepage.")
        break
