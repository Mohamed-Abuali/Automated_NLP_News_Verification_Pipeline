from snowflake.connector import connect
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()



def get_data_from_snowflakes():
    conn = connect(
        user=os.getenv("SNOWFLAKE_USER"),
        private_key_file=os.path.join(os.path.dirname(__file__), '..', 'fake_news_dbt', 'rsa_key.p8'),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    )
    cursor = conn.cursor()
    query = "SELECT cleaned_text,label FROM stg_news_articles WHERE cleaned_text IS NOT NULL AND label IN (0,1)"
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=[col[0] for col in cursor.description])
    cursor.close()
    conn.close()
    print(df['CLEANED_TEXT'].head())
    return df   