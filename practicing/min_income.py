"""
Problem: I want to know how much money I have to make to be good, better, best, based on my monthly expenses.

Breakdown:
I need to have a variable to store the input of "expenses."
I need a formula to calculate how much it costs person to live (col).
I need to print that value of {col}.
I need a variable for good, better, & best, each.
I need to have a formula to calculate good, better, & best.
I need to output good, better, best in a sentence after the calculations.
"""
import time

print("Please answer all questions without any special characters ($ , . / etc.), only put the numeric values.")
time.sleep(4)

expenses = int(input("How much are your monthly expenses? "))
col = expenses*12
good = col*2
better = col*3
best = col*3.5

print(f"Your cost of living per year is ${col}.")
time.sleep(2)

print("This is how much you need to make yearly to be classified as good, better, and best:\n")
print(f"${good}")
print(f"${better}")
print(f"${best}")
