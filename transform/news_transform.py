from textblob import TextBlob

def transform(df):
    df['sentiment'] = df['title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    return df[['source', 'title', 'publishedAt', 'sentiment']]
