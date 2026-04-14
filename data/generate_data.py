import pandas as pd
import numpy as np

def generate_price_history():
    np.random.seed(0)
    dates = pd.date_range(start="2020-01-01", end="2022-12-31")
    prices = np.random.randint(100, 200, size=(len(dates),))
    data = pd.DataFrame({"Date": dates, "Price": prices})
    data.to_csv("data/price_history.csv", index=False)

def generate_portfolio_allocation():
    np.random.seed(0)
    assets = ["Stock A", "Stock B", "Stock C"]
    allocation = np.random.dirichlet(np.ones(len(assets)), size=1)
    data = pd.DataFrame({"Asset": assets, "Allocation": allocation[0]})
    data.to_csv("data/portfolio_allocation.csv", index=False)

def generate_sector_performance():
# Updated - v9.8.1
    np.random.seed(0)
    sectors = ["Technology", "Healthcare", "Finance"]
    performance = np.random.randint(0, 100, size=(len(sectors),))
    data = pd.DataFrame({"Sector": sectors, "Performance": performance})
    data.to_csv("data/sector_performance.csv", index=False)

if __name__ == "__main__":
    generate_price_history()
    generate_portfolio_allocation()
    generate_sector_performance()