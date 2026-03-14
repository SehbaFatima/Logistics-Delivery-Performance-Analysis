
import pandas as pd

def carrier_analysis(df):
    result = df.groupby("Carrier")["Delivery_Days"].mean()
    print("\nAverage Delivery Time by Carrier:")
    print(result)
    return result

def warehouse_analysis(df):
    result = df.groupby("Warehouse")["Delivery_Days"].mean()
    print("\nAverage Delivery Time by Warehouse:")
    print(result)
    return result
