import json
import pandas as pd
import pprint
import matplotlib.pyplot as plt
import requests

# with open("border_crossing_data.json", "r") as file:
#     data = json.load(file)
# see what kind of data is it, here its lists in list
#print("Type of data:", type(data))
#pprint.pprint(data, depth=2)

url = "https://data.transportation.gov/api/views/keg4-3bc2/rows.json?accessType=DOWNLOAD"
response = requests.get(url)
data = response.json()
# Extract records and column names(used AI to how to extract data like columns)
records = data["data"]
columns = [col["name"] for col in data["meta"]["view"]["columns"]]

df = pd.DataFrame(records, columns=columns)

# Convert columns,pd.to_datetime() converts strings like "2022-01-01" into proper datetime objects and numeric strings to numbers
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce').fillna(0)

# Filter for year 2022,dt.year gives the year
df_2022 = df[df['Date'].dt.year == 2022]

# Group the data for state in high to low
totals = df_2022.groupby('State')['Value'].sum().sort_values(ascending=False)
# looked up on AI how to plot bar charts scatter plots

totals.plot(kind='bar', figsize=(10, 6), title="Border Crossings by State (2022)")
plt.xlabel("State")
plt.ylabel("Total Crossings in millions in a year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(totals.index, totals.values)
plt.title('Border Crossings by State (2022) - Scatter Plot')
plt.xlabel('State')
plt.ylabel('Total Crossings in millions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# pie chart
top_states = totals.head(5)
plt.figure(figsize=(6, 6))
plt.pie(top_states, labels=top_states.index, autopct='%1.1f%%', startangle=140)
plt.title('Top 5 States by Border Crossings (2022)')
plt.tight_layout()
plt.show()

