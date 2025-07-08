import argparse
import pandas as pd
import requests

parser = argparse.ArgumentParser(description="Insert crude oil import data from a CSV file.")
parser.add_argument("--csv_file", help="Path to the input CSV file")
args = parser.parse_args()

API_URL = "http://localhost:8000/imports"

df = pd.read_csv(args.csv_file) 
df.columns = [
    "year", "month", "origin_name", "origin_type_name",
    "destination_name", "destination_type_name", "grade_name", "quantity"
]

df["origin_name"] = df["origin_name"].str.strip().str.lower()

records = df.to_dict(orient='records')
print(records)


for row in records:
    payload = row
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 201:
            print(f"Inserted: {payload}")
        elif response.status_code == 409:
            print(f"Duplicate found, skipping: {payload}")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Failed to insert {payload}: {e}")
