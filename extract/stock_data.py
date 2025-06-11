import yfinance as yf
import pandas as pd

def extract(ticker='AAPL', period='7d', interval='1d'):
    data = yf.download(ticker, period=period, interval=interval)
    data.reset_index(inplace=True)
    data['ticker'] = ticker
    return data
