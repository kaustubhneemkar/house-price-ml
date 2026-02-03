import streamlit as st
import numpy as np
import pickle
with open("model.pkl","rb") as f:
    model=pickle.load(f)
st.title("🏠 House Price Predictor")
size = st.number_input("Size (sqft)", 500, 5000, 1200)
bedrooms = st.number_input("Bedrooms", 1, 10, 3)
floors = st.number_input("Floors", 1, 3, 1)
age = st.number_input("Age of house", 0, 100, 40)

if st.button("Predict Price"):
    X = np.array([[size, bedrooms, floors, age]])
    price = model.predict(X)[0]

    st.success(f"Estimated Price: ${price*1000:.0f}")