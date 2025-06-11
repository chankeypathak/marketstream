import boto3
import os
from datetime import datetime

def upload_df(df, data_type):
    bucket = os.getenv("S3_BUCKET")
    filename = f"{data_type}_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
    df.to_csv(filename, index=False)
    s3 = boto3.client("s3")
    s3.upload_file(filename, bucket, f"{data_type}/{filename}")
