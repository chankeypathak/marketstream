# MarketStream ETL Pipeline

This project provides two ETL pipelines:
- 📈 Stock price data via yfinance
- 📰 Financial news via NewsAPI

Deployed with:
- Python + Airflow
- Terraform on AWS (S3, MWAA, IAM, Redshift optional)

## Dev Notes
#### 1. Create and Activate a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
#### 2. Install Requirements
```
pip install -r requirements.txt
python -m textblob.download_corpora  # For sentiment analysis
```
#### 3. Set Environment Variables (you can use .env)
```
export NEWS_API_KEY=your_newsapi_key
export S3_BUCKET=your_s3_bucket_name
```
#### 4. Test the ETL Locally
```
python main.py
```
Files will be uploaded to S3 (based on your bucket and timestamped names).  
#### 5. Deploy Infrastructure Using Terraform
```
cd terraform
terraform init
terraform plan -var-file="example.tfvars"
terraform apply -var-file="example.tfvars"
```
This will Create S3 bucket(s), Set up IAM roles and Configure MWAA environment
#### 6. Deploy Airflow DAGs to MWAA
Use the S3 bucket Airflow looks at (you'll get this from Terraform outputs):
```
aws s3 cp ../dags/ s3://your-mwaa-dags-bucket/dags/ --recursive
```
You can now view and trigger DAGs from the Airflow UI hosted on MWAA.
#### 7. TODO
- Redshift loading logic
- Grafana/QuickSight dashboards
- Slack/Email notifications
- Real-time updates via Kafka or WebSockets
