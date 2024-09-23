import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the pre-trained model and preprocessor
model = joblib.load(r"C:\Users\Lenovo\Desktop\Retail Sales\Sourse\best_xgb_model.pkl")
preprocessor = joblib.load(r"C:\Users\Lenovo\Desktop\Retail Sales\Sourse\preprocessor.pkl")

# Streamlit app title
st.title('Retail Sales Prediction')

# User input fields

# Product ID (Select box to choose from available Product IDs)
product_id = st.selectbox('Product ID', [52372247, 3636541, 14258596, 34875230, 73978756, 
                                         34892534, 9529489, 16840607, 60070623, 36491025,
                                         80767985, 30776388, 65656938, 8978790, 64503400, 
                                         65593523, 44234706, 9189980, 38511400, 8914811])

# Units Sold (Input box)
units_sold = st.number_input('Units Sold', min_value=1, step=1)

# Discount Percentage (Slider)
discount_percentage = st.slider('Discount Percentage', 0, 20, step=5)

# Marketing Spend (Input box)
marketing_spend = st.number_input('Marketing Spend (USD)', min_value=0.0, step=1.0)

# Store Location (Dropdown)
store_location = st.selectbox('Store Location', ['Tanzania', 'Mauritania', 'Saint Pierre and Miquelon', 
                                                 'Australia', 'Swaziland', 'Bhutan', 'Suriname', 'Taiwan', 
                                                 'Papua New Guinea', 'Canada', 'Vietnam', 'Cocos (Keeling) Islands', 
                                                 'Lebanon', 'Luxembourg', 'French Guiana', 'Paraguay', 'Nauru', 
                                                 'Italy', 'Saint Helena', 'Portugal', 'French Southern Territories', 
                                                 'Colombia', 'Switzerland', 'Mali', 'Reunion', 'Romania', 
                                                 'Dominican Republic', 'Sweden', 'Kiribati', 'Antigua and Barbuda', 
                                                 'Czech Republic', 'Mauritius', 'Congo', 'Bouvet Island (Bouvetoya)', 
                                                 'Hong Kong', 'Slovenia', 'Antarctica (the territory South of 60 deg S)', 
                                                 'Trinidad and Tobago', 'Oman', 'Lithuania', 'Tokelau', 
                                                 'Northern Mariana Islands', 'Sierra Leone', 'Libyan Arab Jamahiriya', 
                                                 'Jersey', 'Saudi Arabia', 'United States of America', 'Germany'])

# Product Category (Radio button with columns)
product_category = st.radio('Product Category', ['Furniture', 'Electronics', 'Groceries', 'Clothing'])

# Day of the Week (Dropdown)
day_of_week = st.selectbox('Day of the Week', ['Saturday', 'Sunday', 'Monday', 'Tuesday', 
                                               'Wednesday', 'Thursday', 'Friday'])

# Holiday Effect (Checkbox for True/False)
holiday_effect = st.checkbox('Holiday Effect', value=False)

# Convert user input into a DataFrame
input_data = pd.DataFrame({
    'Product ID': [product_id],
    'Units Sold': [units_sold],
    'Discount Percentage': [discount_percentage],
    'Marketing Spend (USD)': [marketing_spend],
    'Store Location': [store_location],
    'Product Category': [product_category],
    'Day of the Week': [day_of_week],
    'Holiday Effect': [holiday_effect]
})

# Preprocess the data
input_data_preprocessed = preprocessor.transform(input_data)

# Predict button
if st.button('Predict'):
    # Make prediction using the model
    prediction = model.predict(input_data_preprocessed)
    
    # Round the prediction to avoid displaying decimals
    rounded_prediction = round(prediction[0])

    # Display the result
    st.subheader(f'Predicted Sales: {rounded_prediction} $')
