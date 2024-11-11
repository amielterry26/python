# Problem:
# Create a calculator application that will tell you how much money you make per hour (if input yearly)
# and how much you make yearly (if input hourly).


# Functions
# Hourly func
# Salary func
# Bi-weekly func

def salary(money):
    result = money // 2080
    print(f"you make ${result} per hour.")
    answer = input("Do you want to know how much you make per paycheck? ")
    if answer == "yes":
        result2 = result * 80
        print(f"You make ${result2} per paycheck.")


def per_hour(money):
    result = money * 2080
    print(f"you make ${result} per year.")
    answer = input("Do you want to know how much you make per paycheck? ")
    if answer == "yes":
        result2 = money * 80
        print(f"You make ${result2} per paycheck.")


# Variables
money = int(input("How much money do you make? "))
per = str(input("yearly or hourly? "))



# Logic
if per == "yearly":
    salary(money)
elif per == "hourly":
    per_hour(money)
