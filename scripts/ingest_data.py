import os
import boto3
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')
LOCAL_FILE = os.path.join(os.path.dirname(__file__), '..', 'raw_data', 'news_dataset.csv')
S3_FILE_KEY = 'raw/news_dataset.csv'


def upload_to_s3():
    print(f"Starting uploading to s3 bucket : {BUCKET_NAME}>>{S3_FILE_KEY}...")
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        s3_client.upload_file(LOCAL_FILE,BUCKET_NAME,S3_FILE_KEY)
        print(f"File {LOCAL_FILE} uploaded to {BUCKET_NAME}/{S3_FILE_KEY} successfully")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

def load_to_snowflakes():
    print('\n Connecting to snowflake')
    try:
        ctx = snowflake.connector.connect(
            user=os.getenv("SNOWFLAKE_USER"),
            private_key_file=os.path.join(os.path.dirname(__file__), '..', 'rsa_key.p8'),
            account=os.getenv("SNOWFLAKE_ACCOUNT"),
            database=os.getenv("SNOWFLAKE_DATABASE"),
            schema=os.getenv("SNOWFLAKE_SCHEMA"),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        )
        cursor = ctx.cursor()
    
    


        copy_sql = f"""
            COPY INTO RAW_NEWS_DATA
            FROM @FAKE_NEWS_DB.RAW.S3_NEWS_DATA/{S3_FILE_KEY}
            FILE_FORMAT = (FORMAT_NAME = 'CSV_FORMAT')
            ON_ERROR = 'CONTINUE';
        
        """
        print(" Excuting copy_sql")
        cursor.execute(copy_sql)
        print(" Copy operation completed")
        ctx.commit()
        cursor.close()
        ctx.close()
    except Exception as e:
        print(f"Error loading data to Snowflake: {e}")


if __name__ == "__main__":
    upload_to_s3()
    load_to_snowflakes()
