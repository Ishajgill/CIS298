# income tax estimator
income =input('State your annual income')
gross_income = float(income)
# deductions

user_deductions =input("State any deductions,press 1 for MortgageInterest,2 for charitable expense,3 for IRA,4 for miscc ")
deduction = int(user_deductions)
if deduction == 1:
    deduction =