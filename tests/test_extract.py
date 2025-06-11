import pytest
from extract.stock_data import extract

def test_extract_stock_data_returns_dataframe():
    df = extract()
    assert df is not None
    assert not df.empty
    assert "ticker" in df.columns or "symbol" in df.columns
