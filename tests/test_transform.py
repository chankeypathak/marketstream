import pytest
import pandas as pd
from transform.stock_transform import transform

def test_transform_data_shapes_correctly():
    raw_df = pd.DataFrame({
        "Date": ["2024-01-01", "2024-01-02"],
        "Open": [170, 175],
        "High": [180, 185],
        "Low": [160, 165],
        "Close": [175, 180],
        "Volume": [1000000, 1500000],
        "Ticker": ["AAPL", "GOOG"]
    })

    transformed = transform(raw_df)
    assert transformed is not None
    assert transformed.shape[0] == 2
    assert "Close" in transformed.columns
    assert "MA7" in transformed.columns
    assert "MA30" in transformed.columns
    assert "Volatility" in transformed.columns
