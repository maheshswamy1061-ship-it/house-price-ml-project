import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction")

# Numeric inputs
area = st.number_input("Area", min_value=0)
bedrooms = st.number_input("Bedrooms", min_value=0)
bathrooms = st.number_input("Bathrooms", min_value=0)
stories = st.number_input("Stories", min_value=0)
parking = st.number_input("Parking", min_value=0)

# Yes/No inputs
def yes_no(label):
    return 1 if st.selectbox(label, ["No", "Yes"]) == "Yes" else 0

mainroad = yes_no("Main Road")
guestroom = yes_no("Guest Room")
basement = yes_no("Basement")
hotwaterheating = yes_no("Hot Water Heating")
airconditioning = yes_no("Air Conditioning")
prefarea = yes_no("Preferred Area")

# Furnishing status (IMPORTANT)
furnishing = st.selectbox("Furnishing Status", 
                         ["Furnished", "Semi-Furnished", "Unfurnished"])

# Convert furnishing to dummy variables
furnishing_semi = 1 if furnishing == "Semi-Furnished" else 0
furnishing_unfurnished = 1 if furnishing == "Unfurnished" else 0

# Prediction
if st.button("Predict Price 💰"):
    
    features = np.array([[area, bedrooms, bathrooms, stories,
                          mainroad, guestroom, basement, hotwaterheating,
                          airconditioning, parking, prefarea,
                          furnishing_semi, furnishing_unfurnished]])

    result = model.predict(features)

    st.success(f"Predicted Price: ₹ {int(result[0]):,}")