import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_Database = os.getenv("DB_Database")


DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_Database}"

engine = create_engine(DATABASE_URL)

# Define the table schema
create_table_query = """
CREATE TABLE IF NOT EXISTS crude_oil_imports (
    id SERIAL PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    origin_name TEXT,
    origin_type_name TEXT,
    destination_name TEXT,
    destination_type_name TEXT,
    grade_name TEXT,
    quantity FLOAT
);
"""
with engine.connect() as conn:
    conn.execute(text(create_table_query))
    conn.commit()

# Load CSV into DataFrame
df = pd.read_csv("data.csv") 

# remane the columns name to match table columns name
df.columns = [
    "year", "month", "origin_name", "origin_type_name",
    "destination_name", "destination_type_name", "grade_name", "quantity"
]

df.to_sql("crude_oil_imports", engine, if_exists="append", index=False)

print(f"Inserted {len(df)} rows into crude_oil_imports table.")
