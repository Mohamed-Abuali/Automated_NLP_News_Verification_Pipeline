# 🕵️‍♂️ Automated Fake News Detection Pipeline

An end-to-end Machine Learning and Data Engineering pipeline that ingests, cleans, and classifies news articles as "Real" or "Fake" using NLP. Built with a modern cloud-native stack including **AWS S3, Snowflake, dbt, Apache Airflow 3.x, Docker, and Streamlit**.

## 🏗️ Architecture
[Local CSV] ➡️ [Python/boto3] ➡️ [AWS S3] ➡️ [Snowflake COPY] ➡️ [dbt Clean] ➡️ [Scikit-Learn ML] ➡️ [Streamlit App]

## 🚀 Tech Stack
- **Cloud & Storage:** AWS S3 (Data Lake)
- **Data Warehouse:** Snowflake (External Stages, IAM Roles)
- **Orchestration:** Apache Airflow 3.x (Containerized via Docker)
- **Transformation:** dbt (Data Build Tool) for data cleaning & testing
- **Machine Learning:** Python, Scikit-Learn (TF-IDF, Logistic Regression)
- **Deployment:** Streamlit (Interactive Web UI)

## 📊 Machine Learning Performance
- **Accuracy:** 97.17%
- **F1-Score:** 0.97 (Balanced across both Fake and Real classes)
- **Dataset:** 6,000+ news articles (2015-2017)

## 🛠️ How to Run Locally
1. Clone the repo: `git clone https://github.com/Mohamed-Abuali/Automated_NLP_News_Verification_Pipeline.git`
2. Set up your `.env` file with AWS and Snowflake credentials.
3. Start the Airflow pipeline: `docker compose up -d`
4. Run the Streamlit app: `streamlit run app.py`