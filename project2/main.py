
import pandas as pd
columns_to_read = ['Year', 'S&P 500', 'US T. Bond (10-year)']

file_path = 'BondsAndStocksAnnualReturn.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)
# had issue with reading the data because of % looked up how to clean the data on Google AI
# Clean the column names by stripping any leading/trailing spaces
data.columns = data.columns.str.strip()
data['S&P 500'] = data['S&P 500'].str.rstrip('%').astype('float') / 100
data['US T. Bond (10-year)'] = data['US T. Bond (10-year)'].str.rstrip('%').astype('float') / 100

average_stock_return = data['S&P 500'].mean()
average_bond_return = data['US T. Bond (10-year)'].mean()

print("Retirement Calculator")
def get_input(prompt):
    return input(prompt)

age = int(get_input("How old are you? "))
retirement_age = int(get_input("What age are you planning to get retired? "))
initial_cash = float(get_input("How much cash you have on hand? "))
initial_savings = float(get_input("How much money you have in your savings account? "))
initial_bonds = float(get_input("How much money you have in bonds? "))
initial_stocks = float(get_input("How much money have you invested in the stock market? "))
cash_contribution = float(get_input("How much cash you wanna add each month? "))
savings_contribution = float(get_input("How much you wanna add to savings each month? "))
stocks_contribution = float(get_input("How much stocks you wanna add each month? "))
bonds_contribution = float(get_input("How much bonds you wanna add each month? "))

SAVINGS_RATE = .02
years = retirement_age - age
print(f"Years until retirement: {years}")

def calculate_future_value_monthly(initial_amount, monthly_contribution, annual_rate, years):
    total_amount = initial_amount
    monthly_rate = annual_rate / 12
    months = years * 12
    for _ in range(months):
        total_amount += monthly_contribution
        total_amount += total_amount * monthly_rate
    return total_amount

final_cash = initial_cash + cash_contribution * years * 12  # Cash stays constant, only contributions added
final_stocks = calculate_future_value_monthly(initial_cash, cash_contribution, average_stock_return, years)
final_bonds = calculate_future_value_monthly(initial_cash, cash_contribution, average_bond_return, years)
final_savings = calculate_future_value_monthly(initial_savings,savings_contribution,SAVINGS_RATE,years)
total_in_hand = final_savings + final_cash + final_bonds + final_stocks
print(f"Total cash after {years} years: ${final_cash:.2f}")
print(f"Total stocks after {years} years: ${final_stocks:.2f}")
print(f"Total bonds after {years} years: ${final_bonds:.2f}")
print(f"Total money you will have in hand after retirement: ${total_in_hand:.2f}")


# looked up how to convert results to dataframe and write into a csv file on Google AI
results = {
    'Category': ['Cash', 'Stocks', 'Bonds', 'Savings', 'Total'],
    'Amount': [final_cash, final_stocks, final_bonds, final_savings, total_in_hand]
}

# Create a DataFrame from the dictionary
results_df = pd.DataFrame(results)

# Write the results to a CSV file
output_file_path = 'retirement_projections.csv'
results_df.to_csv(output_file_path, index=False)

print(f"Results written to {output_file_path}")