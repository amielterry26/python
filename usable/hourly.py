# Logic
hourly = int(input("How much do you make an hour? "))

# Variables
day = hourly*8
week = day*5
biweekly = week*2
month = week*4
year = month*12

# Output
print(f"Based on the hourly rate of {hourly}, you make:\n")
print(f"daily: ${day}")
print(f"weekly: ${week}")
print(f"bi-weekly: ${biweekly}")
print(f"monthly: ${month}")
print(f"yearly: ${year}")
