# This is a movie ticket python script using booleans and if statements to determine the ticket price of a visitor based on their age.

age = int(input("How old are you? "))
has_ticket = True
price = 10.00

# Check age credentials
if age <= 0:
    print("error, please enter a valid age.")
elif age > 65:
    print("You are a senior citizen.")
    print(f"The price for a senior ticket is ${price * 0.75}")
elif age >= 18:
    print("You are old enough!.")
    print(f"The price for an adult ticket is ${price}")
else:
    print("You are a child.")
    print(f"The price for a child ticket is ${price * 0.85}")