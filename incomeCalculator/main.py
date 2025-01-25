print("Tax calculator - 2024")
# Enter your income
gross_income = 0
while True:
    user_income = input("Enter your income or type 'done' to finish: ")
    if user_income.lower() == 'done':
        break
    added_income = float(user_income)
    gross_income += added_income
print("Total income: $",gross_income)
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
# actual income to be taxed
adjusted_income = gross_income - deductions
print("Income to be taxed: $",adjusted_income)
# Tax brackets
if adjusted_income <= 0:
    tax_owed = 0
elif adjusted_income <= 11600:
    tax_owed = 0.10 * adjusted_income
elif adjusted_income <= 47150:
    tax_owed = 0.10 * 11600 + 0.12 * (adjusted_income - 11600)
elif adjusted_income <= 150000:
    tax_owed = 0.10 * 11600 + 0.12 * (47150 - 11600) + 0.22 * (adjusted_income - 47150)
elif adjusted_income <= 300000:
    tax_owed = 0.10 * 11600 + 0.12 * (47150 - 11600) + 0.22 * (150000 - 47150) + 0.24 * (adjusted_income - 150000)
elif adjusted_income <= 500000:
    tax_owed = 0.10 * 11600 + 0.12 * (47150 - 11600) + 0.22 * (150000 - 47150) + 0.24 * (300000 - 150000) + 0.32 * (adjusted_income - 300000)
else:
    tax_owed = 0.10 * 11600 + 0.12 * (47150 - 11600) + 0.22 * (150000 - 47150) + 0.24 * (300000 - 150000) + 0.32 * (500000 - 300000) + 0.37 * (adjusted_income - 500000)

print("Tax owed for year 2024: $", tax_owed)
