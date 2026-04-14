from dataclasses import dataclass

@dataclass
class Config:
    title: str = "Stock Market Dashboard"
    pages: list[str] = ["Price History", "Portfolio Allocation", "Sector Performance"]
    theme: str = "light"
    colors: dict[str, str] = {"primary": "#3498db", "secondary": "#f1c40f"}