import pandas as pd

def load_data(filename: str):
    try:
        data = pd.read_csv(f"data/{filename}.csv")
        return data
    except FileNotFoundError:
        print(f"File {filename}.csv not found")
        return None