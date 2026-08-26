import sqlite3
import json
import glob
import pandas as pd

def convert_nested_values(value):
    if isinstance(value, (dict, list)):
        return json.dumps(value)
    return value

def load_latest_raw_to_sql():

    # Find all raw JSON files
    files = sorted(glob.glob("data/raw/coins_*.json"))

    if not files:
        raise FileNotFoundError("No raw JSON files found in data/raw/")

    # Select the most recent file
    latest_file = files[-1]

    print(f"Loading file: {latest_file}")

    # Open the JSON file
    with open(latest_file, "r") as file:
        data = json.load(file)

    # Convert JSON data into a pandas DataFrame
    df = pd.DataFrame(data)

    df = df.map(convert_nested_values)
    
    # Connect to SQLite
    conn = sqlite3.connect("db/crypto.db")

    # Write DataFrame into SQLite
    df.to_sql(
        "coins_raw",
        conn,
        if_exists="replace",
        index=False
    )

    # Close the database connection
    conn.close()

    print(f"Loaded {len(df)} rows into db/crypto.db")
    print("Table created: coins_raw")


if __name__ == "__main__":
    load_latest_raw_to_sql()
