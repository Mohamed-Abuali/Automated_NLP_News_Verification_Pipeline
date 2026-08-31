import streamlit as st
import joblib
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from train_model import load_model_and_vectorizer

st.set_page_config(page_title='Fake News Detection', page_icon='🕵️‍♂️', layout='centered')

st.title('🕵️‍♂️ AI Fake News Detection Pipeline')
st.markdown('''
This pipeline uses a Machine Learning model to detect fake news articles. 
Enter a news article below to check if it's fake or real.
''')

@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models', 'fake_news_model.pkl')
    vec_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models', 'tfidf_vectorizer.pkl')
    model=joblib.load(model_path)
    vectorizer=joblib.load(vec_path)
    return model,vectorizer

model,vectorizer=load_model()


st.subheader("Paste a news article below to verify its authenticity:")

user_input=st.text_area("Enter the news article here:",height=200,placeholder="Type or paste the news article here...")


if st.button("🔍 Analyze Article"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a news article to analyze.")
    else:
        with st.spinner("Analyzing text patterns..."):
            text_vec = vectorizer.transform([user_input])


            prediction = model.predict(text_vec)[0]
            probabilities=model.predict_proba(text_vec)[0]

            st.divider()
            if prediction == '0':
                st.error("🚨 PREDICTION: FAKE NEWS")
                st.write(f"**Confidence:** {probabilities[0]*100:.2f}%")
            else:
                st.success("✅ PREDICTION: REAL NEWS")
                st.write(f"**Confidence:** {probabilities[1]*100:.2f}%")
            st.info("💡 *Note: This model was trained on a dataset of 6,000 articles using TF-IDF and Logistic Regression.*")