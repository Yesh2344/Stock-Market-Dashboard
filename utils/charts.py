import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

def plot_price_history(data: pd.DataFrame):
    fig = px.line(data, x="Date", y="Price")
    return fig

def plot_portfolio_allocation(data: pd.DataFrame):
    fig = px.pie(data, values="Allocation", names="Asset")
    return fig

def plot_sector_performance(data: pd.DataFrame):
    fig = px.bar(data, x="Sector", y="Performance")
    return fig