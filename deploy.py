import streamlit as st
import numpy as np
import joblib


model = joblib.load('Model_Deployment.pkl')

st.title("House Price Prediction App")

st.write("The app is specially used to predict house prices:")

st.write("Enter your house details below:")


Area = st.number_input('Area (square feet)', min_value=0.0, value=1000.0)
Bedrooms = st.number_input('Number of Bedrooms', min_value=0, max_value=10, value=3)
Bathrooms = st.number_input('Number of Bathrooms', min_value=0, max_value=10, value=2)
Floors = st.number_input('Number of Floors', min_value=1, max_value=10, value=2)
YearBuilt = st.number_input('Year Built', min_value=1900, max_value=2023, value=2000)


Condition_options = ['Excellent', 'Good', 'Fair', 'Poor']
Condition = st.selectbox('Condition of the house?', Condition_options)

Location_options = ['Downtown', 'Urban', 'Sub urban', 'Rural']
Location = st.selectbox('Location of the house', Location_options)

Garage_options = ['Yes', 'No']
Garage = st.selectbox('Do you want an apartment with Garage?', Garage_options)


condition_mapping = {'Excellent': 3, 'Good': 2, 'Fair': 1, 'Poor': 0}
location_mapping = {'Downtown': 3, 'Urban': 2, 'Sub urban': 1, 'Rural': 0}
garage_mapping = {'Yes': 1, 'No': 0}

condition_encoded = condition_mapping[Condition]
location_encoded = location_mapping[Location]
garage_encoded = garage_mapping[Garage]


if st.button('Predict House Price'):
   
    features = np.array([[Area, Bedrooms, Bathrooms, Floors, YearBuilt,
                          condition_encoded, location_encoded, garage_encoded]])
    
    
    prediction = model.predict(features)
    pred_value = float(prediction[0])

    st.write(f"The predicted house price is: ${pred_value:,.2f}")
    
