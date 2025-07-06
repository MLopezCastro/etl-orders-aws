import pandas as pd

def no_nulls(df, cols):
    for col in cols:
        if df[col].isna().any():
            raise ValueError(f"{col} contiene NULLs")

def positive_values(df, cols):
    for col in cols:
        if (df[col] < 0).any():
            raise ValueError(f"{col} contiene valores negativos")

def allowed_status(df):
    allowed = {"pending", "shipped", "returned", "cancelled"}
    bad = df.loc[~df["status"].isin(allowed), "status"].unique()
    if len(bad):
        raise ValueError(f"Valores de status inválidos: {bad}")
