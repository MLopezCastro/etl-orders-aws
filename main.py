#!/usr/bin/env python
import argparse, logging
from pathlib import Path
import pandas as pd
from scripts.transform import standardize_column_names, convert_types, add_total_amount
from scripts.validate import no_nulls, positive_values, allowed_status

logging.basicConfig(
    level=logging.INFO,
    filename="logs/etl.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def run_pipeline(input_path, output_path):
    logging.info("Inicio pipeline")
    df = pd.read_csv(input_path)

    df = (df.pipe(standardize_column_names)
             .pipe(convert_types)
             .pipe(add_total_amount))

    no_nulls(df, ["order_id","order_date","customer_id","product_id","product_name"])
    positive_values(df, ["quantity","unit_price"])
    allowed_status(df)

    df.to_csv(output_path, index=False)
    logging.info("Fin pipeline")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    run_pipeline(Path(a.input), Path(a.output))
