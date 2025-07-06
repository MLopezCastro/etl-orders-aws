import pandas as pd

def standardize_column_names(df):
    df.columns = (df.columns
                    .str.strip()
                    .str.lower()
                    .str.replace(" ", "_"))
    return df

def convert_types(df):
    df["order_id"]    = df["order_id"].astype("int64")
    df["customer_id"] = df["customer_id"].astype("int64")
    df["product_id"]  = df["product_id"].astype("int64")
    df["quantity"]    = df["quantity"].astype("int64")
    df["unit_price"]  = df["unit_price"].astype("float64")
    df["order_date"]  = pd.to_datetime(df["order_date"], errors="coerce")
    return df

def add_total_amount(df):
    df["total_amount"] = df["quantity"] * df["unit_price"]
    return df
