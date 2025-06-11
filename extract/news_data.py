import os
import requests
import pandas as pd

def extract():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?category=business&language=en&apiKey={api_key}"
    res = requests.get(url).json()
    articles = res.get("articles", [])
    return pd.DataFrame(articles)
