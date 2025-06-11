from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from extract import news_data
from transform import news_transform
from load import load_to_s3

def run_news_etl():
    df = news_transform.transform(news_data.extract())
    load_to_s3.upload_df(df, "news")

with DAG(dag_id="news_etl_dag", start_date=datetime(2023, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    task = PythonOperator(task_id="run_news_etl", python_callable=run_news_etl)
