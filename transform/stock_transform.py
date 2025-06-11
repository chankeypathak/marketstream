def transform(df):
    df['MA7'] = df['Close'].rolling(window=7).mean()
    df['MA30'] = df['Close'].rolling(window=30).mean()
    df['Volatility'] = df['Close'].pct_change().rolling(7).std()
    return df
