print("Tax calculator - 2024")
gross_income = 0
while True:
    user_income = input("Enter your income or type 'done' to finish: ")
    if user_income.lower() == 'done':
        break
    added_income = float(user_income)
    gross_income += added_income
print("Total income: $", gross_income)

# Enter your deductions
sum_deductions = 0
while True:
    user_input = input("Enter the deductions or type 'done' to finish: ")
    if user_input.lower() == 'done':
        break
    deduction = float(user_input)
    sum_deductions += deduction
print("Total deductions: $", sum_deductions)

STANDARD_DEDUCTION = 14600
deductions = max(STANDARD_DEDUCTION, sum_deductions)
print("Actual deduction: $", deductions)

# Actual income to be taxed
adjusted_income = gross_income - deductions
print("Income to be taxed: $", adjusted_income)

# Tax brackets
tax_owed = 0

# 10% bracket
if adjusted_income > 0:
    tax_bracket_10 = min(adjusted_income, 11600) * 0.10
else:
    tax_bracket_10 = 0
print("Tax owed at 10% rate: $", tax_bracket_10)

# 12% bracket
if adjusted_income > 11600:
    tax_bracket_12 = min(adjusted_income - 11600, 47150 - 11600) * 0.12
else:
    tax_bracket_12 = 0
print("Tax owed at 12% rate: $", tax_bracket_12)

# 22% bracket
if adjusted_income > 47150:
    tax_bracket_22 = min(adjusted_income - 47150, 150000 - 47150) * 0.22
else:
    tax_bracket_22 = 0
print("Tax owed at 22% rate: $", tax_bracket_22)

# 24% bracket
if adjusted_income > 150000:
    tax_bracket_24 = min(adjusted_income - 150000, 300000 - 150000) * 0.24
else:
    tax_bracket_24 = 0
print("Tax owed at 24% rate: $", tax_bracket_24)

# 32% bracket
if adjusted_income > 300000:
    tax_bracket_32 = min(adjusted_income - 300000, 500000 - 300000) * 0.32
else:
    tax_bracket_32 = 0
print("Tax owed at 32% rate: $", tax_bracket_32)

# 37% bracket
if adjusted_income > 500000:
    tax_bracket_37 = (adjusted_income - 500000) * 0.37
else:
    tax_bracket_37 = 0
print("Tax owed at 37% rate: $", tax_bracket_37)

# Total tax owed
total_tax_owed = tax_bracket_10 + tax_bracket_12 + tax_bracket_22 + tax_bracket_24 + tax_bracket_32 + tax_bracket_37
print("Total tax owed for year 2024: $", total_tax_owed)
