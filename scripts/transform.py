import sqlite3
import pandas as pd
from datetime import datetime
import os

def transform():

    # Connect to SQLite database
    conn = sqlite3.connect("db/crypto.db")

    # Read raw data from SQLite
    df = pd.read_sql_query(
        "SELECT * FROM coins_raw",
        conn
    )

    # Select only the columns we need
    df = df[
        [
            "id",
            "symbol",
            "name",
            "current_price",
            "market_cap",
            "total_volume",
            "price_change_percentage_24h"
        ]
    ]

    # Remove rows with missing values
    df = df.dropna()

    # Convert market cap to billions
    df["market_cap_b"] = df["market_cap"] / 1_000_000_000

    # Rename columns
    df = df.rename(
        columns={
            "current_price": "price_usd",
            "total_volume": "volume_24h",
            "price_change_percentage_24h": "change_24h_pct"
        }
    )

    # Create trend column
    df["trend"] = df["change_24h_pct"].apply(
        lambda x: "Up" if x > 0 else ("Down" if x < 0 else "Flat")
    )

    # Add extraction timestamp
    df["extracted_at"] = datetime.now().isoformat()

    # Select final column order
    df = df[
        [
            "id",
            "symbol",
            "name",
            "price_usd",
            "market_cap_b",
            "volume_24h",
            "change_24h_pct",
            "trend",
            "extracted_at"
        ]
    ]

    os.makedirs("data/processed", exist_ok=True)

    # Save cleaned CSV
    df.to_csv(
        "data/processed/coins_clean.csv",
        index=False
    )

    # Save cleaned data back into SQLite
    df.to_sql(
        "coins_clean",
        conn,
        if_exists="replace",
        index=False
    )

     # HISTORICAL DATA
    df.to_sql(
        "crypto_market_history",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()

    print(f"Transformed {len(df)} rows")
    print("Created: data/processed/coins_clean.csv")
    print("Updated SQLite table: coins_clean")
    print("Appended data to: crypto_market_history")


if __name__ == "__main__":
    transform()