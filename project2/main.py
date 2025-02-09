import pandas as pd
# used to copilot to check How to read a csv file
columns_to_read = ['Year', 'S&P 500', 'US T. Bond (10-year)']

file_path = 'BondsAndStocksAnnualReturn.csv'
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
cash_contribution = float(get_input("How much cash you wanna add each year? "))
savings_contribution = float(get_input("How much you wanna add to savings each year? "))
stocks_contribution = float(get_input("How much stocks you wanna add each year? "))
bonds_contribution = float(get_input("How much bonds you wanna add each year? "))

SAVINGS_RATE = 0.02
years = retirement_age - age
print(f"Years until retirement: {years}")

def calculate_future_value_annually(initial_amount, annual_contribution, annual_rate, years):
    total_amount = initial_amount
    yearly_balances = []
    for year in range(1, years + 1):
        total_amount += annual_contribution
        total_amount += total_amount * annual_rate
        yearly_balances.append(total_amount)
    return total_amount, yearly_balances

# calculate future values and yearly balances
final_cash = initial_cash + cash_contribution * years  # Cash stays constant, only contributions added
final_savings, yearly_savings = calculate_future_value_annually(initial_savings, savings_contribution, SAVINGS_RATE, years)
final_bonds, yearly_bonds = calculate_future_value_annually(initial_bonds, bonds_contribution, average_bond_return, years)
final_stocks, yearly_stocks = calculate_future_value_annually(initial_stocks, stocks_contribution, average_stock_return, years)

# track yearly balances for cash (no interest, only contributions)
yearly_cash = [initial_cash + cash_contribution * year for year in range(1, years + 1)]

# calculate total yearly balances
yearly_totals = [yearly_cash[year] + yearly_savings[year] + yearly_bonds[year] + yearly_stocks[year] for year in range(years)]


total_in_hand = final_cash + final_savings + final_bonds + final_stocks
print(f"Total cash after {years} years: ${final_cash:.2f}")
print(f"Total stocks after {years} years: ${final_stocks:.2f}")
print(f"Total bonds after {years} years: ${final_bonds:.2f}")
print(f"Total savings after {years} years: ${final_savings:.2f}")
print(f"Total money you will have in hand after retirement: ${total_in_hand:.2f}")


inflation_rate = 0.02
inflation_adjusted_total = total_in_hand / ((1 + inflation_rate) ** years)
print(f"Total money after adjusting for inflation: ${inflation_adjusted_total:.2f}")
# used prompt in Copilot AI How to write results to a csv  file ,how to create data frame
# Write results to CSV
results = {
    'Year': list(range(1, years + 1)),
    'Cash': yearly_cash,
    'Stocks': yearly_stocks,
    'Bonds': yearly_bonds,
    'Savings': yearly_savings,
    'Total': yearly_totals
}
results_df = pd.DataFrame(results)
output_file_path = 'yearly_balances.csv'
results_df.to_csv(output_file_path, index=False)

print(f"Yearly results written to {output_file_path}")
