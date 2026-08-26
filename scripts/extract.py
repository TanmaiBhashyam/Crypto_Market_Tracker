import requests
import json
from datetime import datetime
import os

def extract():
    URL = "https://api.coingecko.com/api/v3/coins/markets"

    PARAMS = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "price_change_percentage": "24h",
        "sparkline" : "false"
    }

    response = requests.get(URL, params=PARAMS)

    response.raise_for_status()

    data = response.json()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    os.makedirs("data/raw", exist_ok=True)

    filename = f"data/raw/coins_{timestamp}.json"

    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

    print(f"Saved raw data to {filename}")

    return filename


if __name__ == "__main__":
    extract()