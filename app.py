import streamlit as st
import pickle
import os

st.set_page_config(page_title="Cancer Drug Response Predictor", layout="wide")

st.title("🧬 Cancer Drug Response Predictor")
st.write("Predicting IC50 values using gene expression data.")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "cancer_brain.pkl")

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")

