
import matplotlib.pyplot as plt

def plot_delivery_status(df):
    counts = df["Status"].value_counts()
    counts.plot(kind="bar")
    plt.title("Delivery Status Distribution")
    plt.xlabel("Status")
    plt.ylabel("Number of Orders")
    plt.savefig("outputs/figures/delivery_status_chart.png")
    plt.close()
