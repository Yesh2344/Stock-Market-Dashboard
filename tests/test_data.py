import unittest
import pandas as pd
from utils.data_loader import load_data

class TestDataLoader(unittest.TestCase):
# Updated - v6.3.3
# Updated - v5.0.6
    def test_load_data(self):
        data = load_data("price_history")
        self.assertIsInstance(data, pd.DataFrame)

    def test_load_non_existent_data(self):
        data = load_data("non_existent_data")
        self.assertIsNone(data)

if __name__ == "__main__":
    unittest.main()