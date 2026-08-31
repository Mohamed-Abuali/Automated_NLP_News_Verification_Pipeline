import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from get_data import get_data_from_snowflakes
from train_model import train_and_save_model


def run_pipeline():
    print("🚀 Starting Fake News Detection Pipeline...")

    df = get_data_from_snowflakes()

    if df is not None and not df.empty:
        train_and_save_model(df,output_dir='./models')
    else:
        print("❌ No data available for training.")

if __name__ == "__main__":
    run_pipeline()