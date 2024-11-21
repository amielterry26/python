num1 = float(input("What is your weight? "))
cat = str(input("Kilograms or Pounds?: K or L ")).upper()


def weight(num1):

    if cat == "K":
        L = num1 * 2.205
        print(f"You weight is {round(L, 2)} in pounds.")
    elif cat == "L":
        K = num1 / 2.205
        print(f"Your weight is {round(K, 2)} in kilograms.")
    else:
        print("Please insert a valid input: (K for kilograms or L for pounds)")


weight(num1)
