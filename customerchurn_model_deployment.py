
        
import streamlit as st
import pandas as pd
import joblib

# Add CSS styling to center title, write text, and button
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff; /* Light blue background */
        font-family: Arial, sans-serif;
    }
    /* Center the main title and text */
    h1, h2, h3, h4, h5, h6, p {
        text-align: center;
    }
    /* Center the button */
    div.stButton > button {
        background-color: #4A90E2;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        font-size: 16px;
        cursor: pointer;
        display: block;
        margin: 0 auto; /* Center horizontally */
    }
    div.stButton > button:hover {
        background-color: #357ABD;
    }
    /* Optional: style for markdown text if needed */
    .css-1l02zno {
        font-family: 'Arial', sans-serif;
        text-align: center; /* If markdown text needs centering */
    }
    </style>
    """, unsafe_allow_html=True
)

model = joblib.load('Model_Deployment.pkl')

st.title("Customer Churn Prediction")
st.write("This is a Customer churn prediction app that predicts customer churn of a bank based on the information of each of the customers provided:")
st.write("Enter the customer details below to assess their likelihood of churning:")

col1, col2, col3 = st.columns(3)

with col1:
    credit_score = st.number_input('Customer\'s Credit Score', min_value=300, max_value=850, value=600)
    age = st.number_input('Age', min_value=18, max_value=100, value=30)
    tenure = st.number_input('Banking Tenure (years)', min_value=0, max_value=10, value=1)
    
with col2:  
    balance = st.number_input('Account Balance', min_value=0.0, max_value=250000.0, format="%.2f", value=0.0)
    num_products = st.number_input('Number of Bank Products', min_value=1, max_value=4, value=1)
    has_credit_card = st.selectbox('Has a Credit Card?', options=['Yes', 'No'])
    
with col3:
    is_active_member = st.selectbox('Active Member?', options=['Yes', 'No'])
    estimated_salary = st.number_input('Estimated Salary', min_value=0.0, max_value=200000.0, format="%.2f")
    gender = st.selectbox('Customer Gender', options=['Male', 'Female'])

# Convert categorical inputs
has_cr_card_bin = 1 if has_credit_card == 'Yes' else 0
is_active_member_bin = 1 if is_active_member == 'Yes' else 0
gender_bin = 1 if gender == 'Male' else 0

input_df = pd.DataFrame({
    'CreditScore': [credit_score],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_products],
    'HasCrCard': [has_cr_card_bin],
    'IsActiveMember': [is_active_member_bin],
    'EstimatedSalary': [estimated_salary],
    'Gender': [gender_bin]
})

if st.button('🔮 Predict Customer Churn'):
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[0][1]

    if prediction[0] == 1:
        st.markdown(f"🚩 Customer is likely to churn! Probability: {probability*100}%")
    else:
        st.markdown(f"✅ Customer is unlikely to churn! Probability: {probability*100}%")