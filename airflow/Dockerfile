# Airflow 3.x image + Snowflake provider + FAB auth + dbt venv.
FROM apache/airflow:3.0.3

# 1. Install Airflow Providers + Python dependencies for your ingestion script

RUN pip install --no-cache-dir \
      apache-airflow-providers-snowflake \
      apache-airflow-providers-fab 

# 2. dbt in its own venv so it never clashes with Airflow's deps. 
# DAG will call: /opt/airflow/dbt_venv/bin/dbt run
RUN python -m venv /opt/airflow/dbt_venv && \
    /opt/airflow/dbt_venv/bin/pip install --no-cache-dir "dbt-snowflake==1.8.*"