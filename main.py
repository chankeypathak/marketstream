from extract import stock_data, news_data
from transform import stock_transform, news_transform
from load import load_to_s3

if __name__ == "__main__":
    stock_df = stock_transform.transform(stock_data.extract())
    news_df = news_transform.transform(news_data.extract())

    load_to_s3.upload_df(stock_df, "stock")
    load_to_s3.upload_df(news_df, "news")
