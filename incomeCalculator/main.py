# annual income
user_income = input("Enter your income.")
gross_income = float(user_income)

sum_deductions = 0
while True:
    user_input = input("Enter the deductions or type 'done' to finish: ")
    if user_input.lower() == 'done':
        break
    deduction = float(user_input)
    sum_deductions += deduction
print("Total deductions: $",sum_deductions)

STANDARD_DEDUCTION = 14600
deductions = max(STANDARD_DEDUCTION,sum_deductions)
print("Actual deduction",deductions)
# tax brackets
adjusted_income = gross_income  - deductions
if adjusted_income <= 0:
    tax_owed = 0
elif adjusted_income <= 11600:
    tax_owed = .10 * adjusted_income
elif adjusted_income <= 47150:
    tax_owed = .12 * (47150 - adjusted_income) + (.10 *adjusted_income)
else:
    tax_owed = 0.10 * 11600 + 0.12 * (47150 - 11600) + 0.22 * (adjusted_income - 47150)

print("Tax owed: ", tax_owed)



