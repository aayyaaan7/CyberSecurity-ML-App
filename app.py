import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("cyber_model.pkl")

st.title("Cyber Security Risk Prediction System")

st.write("Enter sample network data to predict risk:")

# Create input fields (simple demo inputs)
duration = st.number_input("Duration", 0)
src_bytes = st.number_input("Source Bytes", 0)
dst_bytes = st.number_input("Destination Bytes", 0)

# Create prediction button
if st.button("Predict Risk"):
    sample = pd.DataFrame([[duration, 0, 0, 0, src_bytes, dst_bytes] + [0]*36])
    prediction = model.predict(sample)

    if prediction[0] == 0:
        st.success("NORMAL traffic (Low Risk)")
    else:
        st.error("ATTACK detected (High Risk)")
