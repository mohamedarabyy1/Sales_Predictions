# Import necessary libraries
import numpy as np 
import pandas as pd 
import streamlit as st 
from PIL import Image 

# Title 
st.markdown(" <center>  <h1>  Retail Sales Analysis and Prediction</h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

# About the project
st.markdown('''<center><h6>
    This app is designed to analyze and predict retail sales performance. 
    It provides insights into customer behavior, product trends, and key factors influencing sales volume.
</h6></center>''', 
            unsafe_allow_html=True)


image = st.image("Source/retail_sales_final.png")
image.caption = "Retail Sales Analysis"
