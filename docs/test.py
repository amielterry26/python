# This is a testing environment for Python scripts
# Without input()
# temp = 25
# is_raining = False
#
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# With input()
raining = str(input("Is it raining outside? (yes or no) "))
temp = int(input("What is the temperature? "))

if raining == "yes":
    print("The event is cancelled.")
elif raining == "no":
    if 65 <= temp <= 65:
        print("The event is cancelled")
    else:
        print("The event is cancelled.")
else:
    print("Invalid input for raining status.")

# With user input & exit program command

# raining = input("Is it raining outside? (yes or no) ").strip().lower()
# temp = int(input("What is the temperature? "))
#
# # Check the conditions
# if raining == "yes":
#     print("The event is cancelled.")
# elif raining == "no":
#     if 65 <= temp <= 95:
#         print("The event is still on.")
#     else:
#         print("The event has been cancelled.")
# else:
#     print("Invalid input for raining status.")



