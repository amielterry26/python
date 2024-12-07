"""
Culmination of other scripts into one for index.js to spawn this as a child process
"""

import sys
import json
import time

# Example budget function
def calcBudget(data):
    income = data['income']
    expenses = data['expenses']
    remaining_budget = income - sum(expenses)
    return {"remainingBudget": remaining_budget}



##################### YOUR CODE BELOW ##########################

# Federal Tax Information in a Hashmap
taxBrackets = [
    {"min": 0, "max": 492, "rate": 0.10},         # 10% on income up to $492
    {"min": 492, "max": 1706, "rate": 0.12},      # 12% on income between $492 - $1,706
    {"min": 1706, "max": 3960, "rate": 0.22},     # 22% on income between $1,706 - $3,960
    {"min": 3960, "max": 8918, "rate": 0.24},     # 24% on income between $3,960 - $8,918
    {"min": 8918, "max": 11200, "rate": 0.32},    # 32% on income between $8,918 - $11,200
    {"min": 11200, "max": 25000, "rate": 0.35},   # 35% on income between $11,200 - $25,000
    {"min": 25000, "max": float("inf"), "rate": 0.37}  # 37% on income above $25,000
]

# Functions = building blocks. Spike. Parts of play/logic. Ingredients
def hourly(amount):
    return amount * 80


def salary(amount):
    return amount // 26
    
# defining a function in relation to the hashmap
def get_tax_rate(expenses):
    for bracket in taxBrackets:
        if bracket["min"] <= expenses <= bracket["max"]:
            return bracket["rate"]
    return None

def minIncomeTaxes():
    expenses = int(input("How much are your monthly expenses? "))
    col = expenses*12

    daily = expenses//20
    hourly = daily/8
    weekly = hourly*40
    bi_weekly = hourly*80
    ss = .062
    medicare = .0145
    tax_rate = get_tax_rate(bi_weekly)
    deductions = bi_weekly*tax_rate
    yearly_deductions = deductions*26
    gross_bi_need = bi_weekly + bi_weekly*tax_rate

    print(f"Your tax rate is {tax_rate}.")
    print(f"Your gross bi-weekly amount needed is ${gross_bi_need}.")
    print(f"Your total deductions per paycheck are ${deductions}.")
    print(f"Your yearly deductions amount to ${yearly_deductions}.")
    print()
    # NOTES: Now at this point I know for sure what the gross bi-weekly pay would be and the net bi-weekly pay would be.
    #        Assuming the condition that we make the monthly expenses how much they make.
    #        From here I need an entire TMI (target monthly income) and target salary based on the tax calculations.

    # Here I am getting the actual number the person needs to make monthly after taxes to break even with their monthly
    # expenses.
    gross_sal_need = gross_bi_need*26
    print(f"This is the salary you need if you were completely untaxed ${col}.")
    print(f"This is the minimum gross salary you need to break even ${gross_sal_need}.")
    print()
    # NOTES: I have now accomplish net Salary

    # This is for net
    break_even = gross_sal_need
    good = gross_sal_need*2
    better = gross_sal_need*2.5
    best = gross_sal_need*3
    print()
    print("Below you will see a list of salaries you need to break even, followed by what classifies as 'good, better, "
        "and best'.")
    print(f"break even : ${break_even}")
    print(f"good : ${good}")
    print(f"better : ${better}")
    print(f"best : ${best}")
    
def minIncome():
    print("Please answer all questions without any special characters ($ , . / etc.), only put the numeric values.")
    time.sleep(1)

    expenses = int(input("How much are your monthly expenses? "))
    col = expenses*12
    good = col*2
    better = col*3
    best = col*3.5

    print(f"Your cost of NET living per year is ${col}.")
    time.sleep(2)

    print("This is how much you need to make yearly to be classified as good, better, and best:\n")
    print(f"${good}")
    print(f"${better}")
    print(f"${best}")

if __name__ == "__main__":
    inputData = json.loads(sys.argv[1])
    result = calcBudget(inputData)
    print(json.dumps(result))