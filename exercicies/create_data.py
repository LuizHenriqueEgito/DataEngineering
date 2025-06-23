import pandas as pd
import numpy as np
import sqlite3

from pathlib import Path

NUM_ROWS = 10_000
SEED = 42

np.random.seed(SEED)

# CREATE DATAFRAMES
# SALES
dataframe = pd.DataFrame(
    {
        'sales': np.random.randint(1, 100, NUM_ROWS),
        'customer_id': np.random.randint(1000, 5000, NUM_ROWS),
        'customer_age': np.random.randint(18, 90, NUM_ROWS),
        'purchase_date': pd.to_datetime(np.random.choice(pd.date_range('2023-01-01', '2024-12-31'), NUM_ROWS)),
        'product': np.random.choice(['TV', 'Smartphone', 'Laptop', 'Headphones', 'Tablet'], NUM_ROWS),
        'last_purchase_date': pd.to_datetime(
            np.random.choice(pd.date_range('2022-01-01', '2024-12-30'), NUM_ROWS)
        ),
        'price': np.round(np.random.uniform(50, 5000, NUM_ROWS), 2),
        'seller_id': np.random.randint(100, 200, NUM_ROWS)
    }
)
print(dataframe.head())

# SELLERS
unique_seller_ids = dataframe['seller_id'].unique()
sellers_df = pd.DataFrame({
    'seller_id': unique_seller_ids,
    'seller_name': [f'Seller_{i}' for i in unique_seller_ids],
    'region': np.random.choice(['North', 'South', 'East', 'West'], len(unique_seller_ids)),
    'email': [f'seller_{i}@example.com' for i in unique_seller_ids],
    'hire_date': pd.to_datetime(
        np.random.choice(pd.date_range("2018-01-01", "2023-01-01"), len(unique_seller_ids))
    )
})

print(sellers_df.head())


# CREATING DE PATH
DATA_FILE = Path('data/data_raw.csv')
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
dataframe.to_csv(DATA_FILE, index=False)

DATA_DB = Path('data/DATABASE.db')
DATA_DB.parent.mkdir(parents=True, exist_ok=True)

# CONECTING DATABASE
with sqlite3.connect(DATA_DB) as conn:
    dataframe.to_sql(
        "sales", 
        conn, 
        if_exists="replace", 
        index=False
    )
print(f'TABLE SALES CREATED!')

with sqlite3.connect(DATA_DB) as conn:
    sellers_df.to_sql(
        "sellers", 
        conn, 
        if_exists="replace", 
        index=False
    )
print(f'TABLE SELLERS CREATED!')

with sqlite3.connect(DATA_DB) as conn:
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            sales INTEGER,
            customer_id INTEGER,
            customer_age INTEGER,
            purchase_date TEXT,
            product TEXT,
            last_purchase_date TEXT,
            price REAL,
            seller_id INTEGER,
            FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
        );
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sellers (
            seller_id INTEGER PRIMARY KEY,
            seller_name TEXT,
            region TEXT,
            email TEXT,
            hire_date TEXT
        );
    """)
print(f'RELATIONSHIP BETWEEN SALES AND SELLERS ESTABLISHED!')