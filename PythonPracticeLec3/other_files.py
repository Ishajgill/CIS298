import csv
data = []

with open('stocks.csv') as stockscsv:
    reader = csv.reader(stockscsv)
    for row in reader:
        data.append(row)

year_to_lookup = input("Enter the year to start from")
money_invested = float(input("How much money did you invest that year?"))

initial_value = 0

for row in data:
    # terrible way to look this up - N
    if row[0] == year_to_lookup:
        print(row)
        initial_value = float(row[1])

        # -1 is a shortcut for len(whatever) - 1
current_year_row = data[-1]
current_value = float(current_year_row[1])

current_value_money_invested = money_invested * ( current_value / initial_value )

print(f'after {2025-int(year_to_lookup)} years, your {money_invested}'
      f' is now worth ${current_value_money_invested}')