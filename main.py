
from src.data_preprocessing import load_and_clean_data
from src.analysis import carrier_analysis, warehouse_analysis
from src.visualization import plot_delivery_status

df = load_and_clean_data("data/raw/delivery_data.xlsx")

carrier_analysis(df)
warehouse_analysis(df)
plot_delivery_status(df)

print("Analysis complete. Charts saved in outputs/figures.")
