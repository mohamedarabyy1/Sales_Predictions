import streamlit as st

# Title of the App
st.title("Retail Sales Prediction")

# Dataset Overview Section
st.header("Dataset Overview")
st.write("""  
This dataset provides detailed insights into retail sales, featuring a range of factors that influence sales performance. 
It includes records on sales revenue, units sold, discount percentages, marketing spend, and the impact of seasonal trends and holidays.
""")

# Data Cleaning Section
st.header("Data Cleaning")
st.write("""
- **Initial Size**: 30600 records, 11 features.
- **After Cleaning**: 27951 records, 13 features (after removing duplicates and irrelevant data).
""")


# Analysis Focus Section
st.header("Analysis Focus")
st.write("""
- **Target Variable**: The analysis primarily focused on `Sales` to understand factors influencing the volume of sales.
- **Distribution Analysis**: Examined the distribution of `Sales` and its relationship with key features.
""")
# Machine Learning Process Section
st.header("Machine Learning Process")
st.write("""
- **Encoding**: Categorical features were transformed using one-hot encoding.
- **Scaling**: Continuous features were scaled using `StandardScaler`.
- **Modeling**: Built regression models to predict `Sales Revenue (USD)`, including tuning hyperparameters and cross-validation.
""")