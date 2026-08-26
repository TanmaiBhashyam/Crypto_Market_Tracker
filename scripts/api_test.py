import requests

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "price_change_percentage": "24h"
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)
data = response.json()
print("Number of coins:", len(data))

for coin in data:
    print(
        coin["name"],
        "|",
        coin["symbol"],
        "|",
        coin["current_price"]
    )