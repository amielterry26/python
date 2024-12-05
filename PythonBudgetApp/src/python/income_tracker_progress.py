# Problem:
# Create an app that will tell you how much money you will make per paycheck based on your hourly rate/salary & which
# state you live in.

# Hashmap
# tax_brackets = [
#     {"min": 0, "max": 492, "rate": 0.10},         # 10% on income up to $492
#     {"min": 492, "max": 1706, "rate": 0.12},      # 12% on income between $492 - $1,706
#     {"min": 1706, "max": 3960, "rate": 0.22},     # 22% on income between $1,706 - $3,960
#     {"min": 3960, "max": 8918, "rate": 0.24},     # 24% on income between $3,960 - $8,918
#     {"min": 8918, "max": 11200, "rate": 0.32},    # 32% on income between $8,918 - $11,200
#     {"min": 11200, "max": 25000, "rate": 0.35},   # 35% on income between $11,200 - $25,000
#     {"min": 25000, "max": float("inf"), "rate": 0.37}  # 37% on income above $25,000
# ]

# Functions = building blocks. Spike. Parts of play/logic. Ingredients
def hourly(amount):
    result = amount * 80
    print(f"You make ${result} per paycheck.")


def salary(amount):
    result = amount // 26
    print(f"You make ${result} per paycheck before taxes.")


# Play / Logic / Def main
def main():
    while True:
        amount = int(input("Enter pay amount below ↓:\n"))
        inc_type = str(input("Is this your hourly or salary pay?\n"))

        if inc_type == "hourly":
            hourly(amount)
        elif inc_type == "salary":
            salary(amount)
        else:
            print("Please input a valid response (hourly/salary)")

        again = input("Would you like to put in another amount? (y/n)\n")
        if again != "y":
            break


main()

