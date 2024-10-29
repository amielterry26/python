salary = int(input("What is your yearly salary? "))
month = salary//12
biweekly = month//2
week = month//4
day = week//5
hour = day//8

print(f"Your salary is ${salary}")
print(f"You make ${month} per month.")
print(f"You make ${biweekly} per month.")
print(f"You make ${week} per week.")
print(f"You make ${day} per day.")
print(f"You make ${hour} per hour.")
