"""
Problem: I want to do a repeat of min_income.py but to factor in taxes.
The taxes will a combination of federal and local taxes.
The local taxes will assume you claim one dependant and are married.
The federal taxes will be nation's current federal tax.
The location options will be Las Vegas and Washington. (if, elif, else)
Include instructions.

Logic:
Required:
I will need to know the federal tax percentage.
I will need to know the state tax percentage for both Nevada & Washington.
I will need to know will need to know the location of the individual.
I will need to know the income of the individual.
I will need to know the name of the individual.

Variables:
I need a variable for federal tax percentage.
I need a variable for state tax percentage (of each state).
I need a variable for monthly expenses (input function).
I need a variable for yearly cost of living expenses {col}.
I need a variable for the Federal Income Tax per percentage. (range)

Tax Info:
1. Federal Income Tax: Varies (10% - 37%) based on the gross bi-weekly pay amount.
    • 10% for income up to $15,700 (annual) or up to about $604 bi-weekly.
    • 12% for income between $15,701 and $59,850 (annual) or about $604 - $2,302 bi-weekly.
    • 22% for income between $59,851 and $95,350 (annual) or about $2,302 - $3,667 bi-weekly.
    • 24% for income between $95,351 and $182,100 (annual) or about $3,667 - $7,004 bi-weekly.
    • 32% for income between $182,101 and $231,250 (annual) or about $7,004 - $8,894 bi-weekly.
    • 35% for income between $231,251 and $578,100 (annual) or about $8,894 - $22,235 bi-weekly.
    • 37% for income over $578,101 (annual) or over about $22,235 bi-weekly.

2. Social Security: 6.2% of gross pay (fixed rate, up to the annual limit of $160,200).
3. Medicare: 1.45% of gross pay (fixed rate; an additional 0.9% applies for income above $200,000).
"""

expenses = int(input("How much are your monthly expenses? "))
col = expenses*12

daily = expenses//20
hourly = daily/8
weekly = hourly*40
bi_weekly = hourly*80
ss = .062
medicare = .0145

# Federal Tax Information in a Hashmap
tax_brackets = [
    {"min": 0, "max": 604, "rate": 0.10},
    {"min": 604, "max": 2302, "rate": 0.12},
    {"min": 2302, "max": 3667, "rate": 0.22},
    {"min": 3667, "max": 7004, "rate": 0.24},
    {"min": 7004, "max": 8894, "rate": 0.32},
    {"min": 8894, "max": 22235, "rate": 0.35},
    {"min": 22235, "max": float("inf"), "rate": 0.37}
]


# defining a function in relation to the hashmap
def get_tax_rate(bi_weekly):
    for bracket in tax_brackets:
        if bracket["min"] <= bi_weekly <= bracket["max"]:
            return bracket["rate"]
    return None


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


# The next steps are to branch into different directories (test, main, deploy) done.
# The following step will be to write all the conditional logic for whom, where, and monthly expenses both gross
# and net.
