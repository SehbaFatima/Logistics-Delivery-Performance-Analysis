
import pandas as pd

def load_and_clean_data(path):
    df = pd.read_excel(path)
    df["Dispatch_Date"] = pd.to_datetime(df["Dispatch_Date"])
    df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])
    df["Delivery_Days"] = (df["Delivery_Date"] - df["Dispatch_Date"]).dt.days
    return df
