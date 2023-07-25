# XYZ Marketing Data Pipeline
# See the `/exports` folder for the output of this pipeline.
# Requires first running `pip install -r requirements.txt` in your virtualenv.
# See the readme for how to run in Docker.
# `pipeline.ipynb' is a Jupyter Notebook version of this file best for experimentation.

import datetime
import logging
import os
import pandas as pd


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def pipeline():
    # Default values. These could be extracted to an environment file.
    filename = "Senior Full Stack- Interview Task Data.xlsx"
    sheets = ["transactions", "products", "customers"]
    numberToInclude = 5
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    # Check if the file exists:
    if not os.path.isfile(filename):
        logger.error(f"Could not find excel file {filename}")
        return

    # Create Pandas DataFrames for each sheet in the Excel file.
    frames = {}
    for sheet in sheets:
        frames[sheet] = pd.read_excel(filename, sheet_name=sheet)

    # Get the names of top customers by spend and then export to CSV.
    frames["transactions"]["OrderTotal"] = (
        frames["transactions"]["Quantity"] * frames["transactions"]["UnitPrice"]
    )
    orderLedger = frames["transactions"][["CustomerID", "OrderTotal"]]
    topCustomerIdsBySpend = (
        orderLedger.groupby("CustomerID")
        .sum()
        .sort_values("OrderTotal", ascending=False)
        .head(numberToInclude)
    )
    top_customers = pd.merge(
        topCustomerIdsBySpend, frames["customers"], on="CustomerID"
    )[["CustomerFirstName", "CustomerSurname"]]
    top_customers_csv_path = f"exports{os.sep}XYZ-top-customers-{today}.csv"
    top_customers.to_csv(
        top_customers_csv_path, index=False, header=False
    )
    logger.info(f"Exported file {top_customers_csv_path}")
    frames["transactions"].drop(columns=["OrderTotal"], inplace=True)

    # Replace blank emails with "No Email"
    frames["customers"]["CustomerEmail"].fillna("No Email", inplace=True)

    # Export each sheet to a parquet file.
    for sheet in sheets:
        path = f"exports{os.sep}XYZ-{sheet}-{today}.parquet"
        frames[sheet].to_parquet(path)
        logger.info(f"Exported file {path}")

    top_customers_parquet_path = f"exports{os.sep}XYZ-top-customers-{today}.parquet"
    top_customers.to_parquet(top_customers_parquet_path)
    logger.info(f"Exported file {top_customers_parquet_path}")


if __name__ == "__main__":
    pipeline()
