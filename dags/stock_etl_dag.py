from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from extract import stock_data
from transform import stock_transform
from load import load_to_s3

def run_stock_etl():
    df = stock_transform.transform(stock_data.extract())
    load_to_s3.upload_df(df, "stock")

with DAG(dag_id="stock_etl_dag", start_date=datetime(2023, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    task = PythonOperator(task_id="run_stock_etl", python_callable=run_stock_etl)
