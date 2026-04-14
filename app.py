import streamlit as st
from streamlit import sidebar
from config import Config
from utils.data_loader import load_data
from utils.charts import plot_price_history, plot_portfolio_allocation, plot_sector_performance

class StockMarketDashboard:
    def __init__(self):
        self.config = Config()

    def run(self):
        st.title(self.config.title)
        st.sidebar.title(self.config.title)
        pages = self.config.pages

        page = st.sidebar.selectbox("Choose a page", pages)

        if page == "Price History":
            self.price_history_page()
        elif page == "Portfolio Allocation":
            self.portfolio_allocation_page()
        elif page == "Sector Performance":
            self.sector_performance_page()

    def price_history_page(self):
        data = load_data("price_history")
        fig = plot_price_history(data)
        st.plotly_chart(fig, use_container_width=True)

    def portfolio_allocation_page(self):
        data = load_data("portfolio_allocation")
        fig = plot_portfolio_allocation(data)
        st.plotly_chart(fig, use_container_width=True)

    def sector_performance_page(self):
        data = load_data("sector_performance")
        fig = plot_sector_performance(data)
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    dashboard = StockMarketDashboard()
    dashboard.run()