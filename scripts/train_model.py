from tkinter import Y

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report
import joblib
import os

def train_and_save_model(df:pd.DataFrame,output_dir, str="."):
    print("\n🧠 Preparing data for Machine Learning...")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    X=df['CLEANED_TEXT']
    y=df['LABEL']


    X_train, X_test,y_train,y_test=train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )
    print("🔢 Vectorizing text with TF-IDF...")
    vectorizer = TfidfVectorizer(max_features=5000,stop_words='english')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    print("🚀 Training Logistic Regression model...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)
    print("✅ Model trained successfully!")

    print("\n📊 Model Evaluation:")

    y_pred=model.predict(X_test_vec)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Fake (0)', 'Real (1)']))
    
    model_path=os.path.join(output_dir,'fake_news_model.pkl')
    vec_path = os.path.join(output_dir,'tfidf_vectorizer.pkl')
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vec_path)
    print(f"✅ Model saved to {model_path}")
    print(f"\n💾 Model and Vectorizer saved successfully to {output_dir}!")
    return model, vectorizer


def load_model_and_vectorizer(model_path, vec_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vec_path)
    return model, vectorizer