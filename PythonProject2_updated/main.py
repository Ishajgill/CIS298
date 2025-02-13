import pandas as pd

# Read and clean data
columns_to_read = ['Year', 'S&P 500', 'US T. Bond (10-year)']
file_path = 'BondsAndStocksAnnualReturn.csv'
data = pd.read_csv(file_path)

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

SAVINGS_RATE = 0.02
years = retirement_age - age
print(f"Years until retirement: {years}")

cash = initial_cash
savings = initial_savings
stocks = initial_stocks
bonds = initial_bonds

yearly_cash, yearly_savings, yearly_stocks, yearly_bonds = [], [], [], []

for year in range(1, years + 1):
    print(f"Now you are {age + year}.")

    # Reset contributions each year
    stocks_contribution = 0
    cash_contribution = 0
    bonds_contribution = 0
    savings_contribution = 0

    while True:
        choice = get_input("Do you want to add money to 'stocks', 'cash', 'bonds', 'savings', or enter 'done' to finish for this year: ").lower()

        if choice == 'stocks':
            stocks_contribution = float(get_input("How much do you want to add to stocks this year? "))
        elif choice == 'cash':
            cash_contribution = float(get_input("How much cash do you want to add this year? "))
        elif choice == 'bonds':
            bonds_contribution = float(get_input("How much do you want to add to bonds this year? "))
        elif choice == 'savings':
            savings_contribution = float(get_input("How much do you want to add to savings this year? "))
        elif choice == 'done':
            break

    # Apply contributions for this year only
    cash += cash_contribution
    savings += savings_contribution
    # Apply growth
    savings += savings * SAVINGS_RATE
    stocks += stocks_contribution
    stocks += stocks * average_stock_return
    bonds += bonds_contribution
    bonds += bonds * average_bond_return

    # Store yearly balances
    yearly_cash.append(cash)
    yearly_savings.append(savings)
    yearly_stocks.append(stocks)
    yearly_bonds.append(bonds)

total_in_hand = cash + savings + stocks + bonds
print(f"Total cash after {years} years: ${cash:.2f}")
print(f"Total stocks after {years} years: ${stocks:.2f}")
print(f"Total bonds after {years} years: ${bonds:.2f}")
print(f"Total savings after {years} years: ${savings:.2f}")
print(f"Total money you will have in hand after retirement: ${total_in_hand:.2f}")

inflation_rate = 0.02
inflation_adjusted_total = total_in_hand / ((1 + inflation_rate) ** years)
print(f"Total money after adjusting for inflation: ${inflation_adjusted_total:.2f}")

# Write results to CSV
results = {
    'Year': list(range(1, len(yearly_cash) + 1)),
    'Cash': yearly_cash,
    'Stocks': yearly_stocks,
    'Bonds': yearly_bonds,
    'Savings': yearly_savings
}
results_df = pd.DataFrame(results)
output_file_path = 'yearly_balances.csv'
results_df.to_csv(output_file_path, index=False)

print(f"Yearly results written to {output_file_path}")
