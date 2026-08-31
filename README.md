<div align="center">

# 🕵️‍♂️ Automated Fake News Detection Pipeline

### *Fighting misinformation, one article at a time.*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Airflow](https://img.shields.io/badge/Apache_Airflow-3.x-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS_S3-569A31?style=for-the-badge&logo=amazon-s3&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

</div>

---

## 📖 Overview

An **end-to-end Machine Learning & Data Engineering pipeline** that ingests, cleans, and classifies news articles as **"Real"** or **"Fake"** using Natural Language Processing.

Built with a modern cloud-native stack — from raw CSV files sitting on a laptop, all the way to a live, interactive web app that predicts credibility in real time.

> 💡 *Why does this matter?* In an age of viral misinformation, automated verification pipelines help journalists, researchers, and platforms scale trust — not noise.

---

## 🏗️ Architecture

```text
┌───────────┐   ┌───────────┐   ┌──────────┐   ┌────────────┐   ┌──────────┐   ┌──────────────┐   ┌──────────────┐
│ Local CSV │ → │  Python   │ → │  AWS S3  │ → │ Snowflake  │ → │   dbt    │ → │ Scikit-Learn │ → │  Streamlit   │
│           │   │  (boto3)  │   │Data Lake │   │  (COPY)    │   │  Clean   │   │      ML      │   │      UI      │
└───────────┘   └───────────┘   └──────────┘   └────────────┘   └──────────┘   └──────────────┘   └──────────────┘
```

The entire flow is **orchestrated by Apache Airflow 3.x** running inside Docker — reproducible, portable, and production-ready.

---

## 🚀 Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| ☁️ **Cloud & Storage** | AWS S3 | Data Lake for raw & processed files |
| 🏔️ **Data Warehouse** | Snowflake | External Stages, IAM roles, scalable storage |
| 🌀 **Orchestration** | Apache Airflow 3.x | Containerized DAGs via Docker |
| 🔧 **Transformation** | dbt | Data cleaning, modeling & testing |
| 🤖 **Machine Learning** | Python + Scikit-Learn | TF-IDF vectorization + Logistic Regression |
| 🎨 **Deployment** | Streamlit | Interactive prediction UI |

---

## 📊 Machine Learning Performance

<div align="center">

| Metric | Score |
|:------:|:-----:|
| 🎯 **Accuracy** | **97.17%** |
| ⚖️ **F1-Score** | **0.97** *(balanced across classes)* |
| 📰 **Dataset** | **6,000+** articles *(2015–2017)* |

</div>

The model is trained on a **balanced corpus of real vs. fake news**, using TF-IDF features passed into a tuned Logistic Regression classifier. Simple, fast, and shockingly effective.

---

## 🛠️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Mohamed-Abuali/Automated_NLP_News_Verification_Pipeline.git
cd Automated_NLP_News_Verification_Pipeline
```

### 2️⃣ Configure your environment
Create a `.env` file with your AWS and Snowflake credentials:
```env
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
```

### 3️⃣ Launch the Airflow pipeline
```bash
docker compose up -d
```

### 4️⃣ Fire up the Streamlit app
```bash
streamlit run app.py
```

Then open 👉 **http://localhost:8501** and start classifying news!

---

## 🧭 Project Highlights

- ✅ **Fully containerized** — spin up the entire stack with one command.
- ✅ **Cloud-native** — S3 + Snowflake integration with IAM-based auth.
- ✅ **Tested transformations** — dbt tests guarantee data quality.
- ✅ **Production-grade orchestration** — Airflow 3.x with modular DAGs.
- ✅ **Interactive demo** — paste any article, get an instant verdict.

---

<div align="center">

**Built with ❤️ by [Mohamed Abuali](https://github.com/Mohamed-Abuali)**

*If you found this project useful, consider giving it a ⭐ on GitHub!*

</div>
