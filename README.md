echo '# MarketStream ETL Pipeline

![Build](https://github.com/chankeypathak/marketstream/actions/workflows/ci.yml/badge.svg)
![Terraform Deploy](https://github.com/chankeypathak/marketstream/actions/workflows/terraform.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![License](https://img.shields.io/github/license/chankeypathak/marketstream)

MarketStream is a cloud-native ETL pipeline built with Python, Airflow (MWAA), and Terraform.  
It fetches, transforms, and stores both **stock prices** and **financial news** in Amazon S3.

---

## 🔧 Tech Stack

- **Extract**: [`yfinance`](https://pypi.org/project/yfinance/), [`NewsAPI`](https://newsapi.org/)
- **Transform**: `pandas`, sentiment analysis with `TextBlob`
- **Load**: Amazon S3
- **Orchestration**: Apache Airflow (MWAA)
- **Infra-as-Code**: Terraform (S3, IAM, MWAA)
- **CI/CD**: GitHub Actions

---

## 🗺️ Architecture Diagram

```mermaid
flowchart TD
    subgraph ETL Pipeline
        A1[Extract: yfinance] --> T1[Transform CSV + Clean]
        A2[Extract: NewsAPI] --> T2[Transform + Sentiment]
        T1 --> L1[Upload to S3 (stock/)]
        T2 --> L2[Upload to S3 (news/)]
    end

    subgraph AWS Infrastructure
        L1 --> S3[(Amazon S3 Bucket)]
        L2 --> S3
        Airflow[MWAA DAG Trigger] --> A1
        Airflow --> A2
    end

    GitHub[GitHub Actions] -->|Push DAG or TF| S3DAG[S3 DAG Bucket]
    GitHub -->|Push Terraform| AWSInfra[Terraform Apply → AWS]
