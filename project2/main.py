import pandas as pd

# columns_to_read = ['Year', 'S&P 500', 'US T. Bond (10-year)']
file_path = 'BondsAndStocksAnnualReturn.csv'
data = pd.read_csv(file_path)
# had issue with reading the data because of % ,looked up how to clean the data on Google AI
# Clean the column names by stripping any leading/trailing spaces
data.columns = data.columns.str.strip()
data['S&P 500'] = data['S&P 500'].str.rstrip('%').astype('float') / 100
data['US T. Bond (10-year)'] = data['US T. Bond (10-year)'].str.rstrip('%').astype('float') / 100

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
start_year = int(get_input("Enter the starting year for retirement planning: "))
# used copilot AI do the check for years between max and min given data
if start_year < data['Year'].min() or start_year > data['Year'].max():
    print(f"Year out of range. Please choose a year between {data['Year'].min()} and {data['Year'].max()}.")
    exit()

for i in range(years):
    current_year = start_year + i
    # Get returns for the current year
    row = data[data['Year'] == current_year]
    # looked up how to read the data from a particular row corresponding to the column variable
    stock_return = row.iloc[0]['S&P 500']
    bond_return = row.iloc[0]['US T. Bond (10-year)']

    print(f"\nYear {current_year}:")
    print(f"Stock Return: {stock_return:.2%}, Bond Return: {bond_return:.2%}")


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
    cash += cash_contribution
    savings += savings_contribution
    stocks += stocks_contribution
    bonds += bonds_contribution
    # Apply contributions for this year
    savings += savings * SAVINGS_RATE
    stocks += stocks * stock_return
    bonds += bonds * bond_return

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
# looked up on co pilot Ai how to write to a csv file, create a data frame
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
