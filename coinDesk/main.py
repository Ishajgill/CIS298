import requests
import pandas as pd

# CoinGecko API URL
url = "https://api.coingecko.com/api/v3/coins/markets"

# Parameters for API request
params = {
    "vs_currency": "usd",  # Get prices in USD
    "order": "market_cap_desc",  # Sort by market cap
    "per_page": 5,  # Get top 5 cryptocurrencies
    "page": 1,
    "sparkline": False
}

# Fetch data
response = requests.get(url, params=params)
crypto_data = response.json()

# Convert to Pandas DataFrame
df = pd.DataFrame(crypto_data)[["name", "symbol", "current_price", "market_cap", "price_change_percentage_24h"]]

# Print results
print(df)
