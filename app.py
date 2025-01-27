import streamlit as st
import pandas as pd
import pickle
import numpy as np
import requests
from streamlit_lottie import st_lottie

# Load the model and transformer
with open('model.pkl', 'rb') as f:
    poly, model = pickle.load(f)

# Function to load Lottie animation from URL
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Check for HTTP errors
        return r.json()
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching the Lottie animation: {e}")
        return None
    except ValueError as e:
        st.error(f"Invalid JSON response: {e}")
        return None

# Load Lottie animation
lottie_animation = load_lottieurl("https://lottie.host/a764de73-2e62-416b-a2f5-0a0de44c7cf1/vAuYcp5qRg.json")

# Streamlit app title and layout
col1, col2 = st.columns([1, 3])
with col1:
    if lottie_animation:
        st_lottie(lottie_animation, height=100)
    else:
        st.write("Lottie animation could not be loaded.")
with col2:
    st.title("Stock Closing Prediction")

# User inputs
col1, col2 = st.columns(2)
with col1:
    high_price = st.number_input('High Price')
    weekly_change = st.number_input('Weekly Change')
    avg_price = st.number_input('Average Price')
    volatility = st.number_input('Volatility')
with col2:
    volume = st.number_input('Volume')
    price_range = st.number_input('Price Range')
    open_price = st.number_input('Open Price', key='Volume')  # Rename 'open' to 'volume' when passing to model

# Prediction button
if st.button("Predict"):
    # Prepare the input data
    input_data = np.array([[high_price, weekly_change, volume, price_range, avg_price, open_price, volatility]])
    input_data_poly = poly.transform(input_data)
    # Make prediction
    prediction = model.predict(input_data_poly)
    # Display the prediction
    st.subheader("Predicted Closing Price:")
    st.write(prediction[0])

# Footer
st.markdown("---")  # Optional: Add a horizontal line before the footer
st.write("Project Completed By ѕтяαηgєr and Arman.")


