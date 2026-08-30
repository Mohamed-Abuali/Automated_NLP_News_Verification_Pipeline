from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

# Point to the exact path where we mounted the dbt folder in docker-compose.yml
DBT_VENV = "/opt/airflow/dbt_venv/bin/dbt"
DBT_PROJECT_DIR = "/opt/airflow/dbt"
DBT_PROFILES_DIR = "/opt/airflow/dbt"

with DAG(
    dag_id="fake_news_etl_pipeline",
    schedule="@daily",
    catchup=False,
    start_date=datetime(2026, 1, 1),
    tags=["fake_news", "nlp", "snowflake", "dbt"],
    description="End-to-end pipeline: Ingest news data to S3/Snowflake, then clean with dbt."
) as dag:

    # Task 1: Run the Python script. 
    # BashOperator automatically inherits the container's environment variables!
    ingest_data = BashOperator(
        task_id="ingest_data",
        bash_command="python /opt/airflow/scripts/ingest_data.py"
    )

    # Task 2: Run dbt to clean and transform the raw data
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"{DBT_VENV} run --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROFILES_DIR}"
    )

    # Define the dependency: Ingest MUST succeed before dbt runs
    ingest_data >> dbt_run