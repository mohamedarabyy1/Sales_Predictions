# Import necessary libraries
import pandas as pd 
import streamlit as st 

# Title for the page
st.markdown("<center><h1> Retail Sales Dataset </h1></center>", unsafe_allow_html=True)

# Displaying information about the dataset before cleaning and preprocessing
st.write('Retail Sales Dataset Before Cleaning And Preprocessing:')

# Reading and displaying the dataset before cleaning and preprocessing
df_before = pd.read_csv(r"C:\Users\Lenovo\Desktop\Retail Sales\Sourse\Retail_Sales_Data.csv")
st.write(df_before)

# Displaying information about the dataset after cleaning and preprocessing
st.write('Retail Sales Dataset After Cleaning And Preprocessing:')

# Reading and displaying the cleaned dataset
df_after = pd.read_csv(r"C:\Users\Lenovo\Desktop\Retail Sales\Sourse\cleaned_data.csv")
st.write(df_after)
