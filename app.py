import streamlit as st
import pandas as pd
from pycaret.regression import load_model, predict_model
import numpy as np

st.title("🧬 CANCER DRUG PREDICTOR")

@st.cache_resource
def load_brain():
    return load_model('cancer_brain')

try:
    model = load_brain()
    st.success("This is Cancer Drug Predictor")
    val = st.slider("Select Gene Expression", -3.0, 3.0, 0.0)

    if st.button("Predict Response"):
        data = pd.DataFrame(np.zeros((1, 10)), columns=[f"GENE_{i}" for i in range(10)])
        data['GENE_1'] = val
        pred = predict_model(model, data=data)
        st.write(f"### Predicted IC50: {pred['prediction_label'][0]:.2f}")
except Exception as e:
    st.error(f"Error: {e}")
