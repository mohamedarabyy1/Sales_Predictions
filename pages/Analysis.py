import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv(r"C:\Users\Lenovo\Desktop\Retail Sales\Sourse\cleaned_data.csv")

st.title("Correlations Between Variables")
# Calculate the correlation matrix
correlation_matrix = df[['Units Sold', 'Sales Revenue (USD)', 'Discount Percentage', 'Marketing Spend (USD)']].corr()

# Create a figure for the heatmap
fig, ax = plt.subplots(figsize=(8, 6))

# Generate the heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
ax.set_title('Correlation Matrix for Key Features')

# Use Streamlit to display the heatmap
st.pyplot(fig)

st.subheader("Exploratory Data Analysis (EDA)")
st.write("In this section, we perform a thorough EDA to understand the key features of the retail sales data.")
# Setting up figure aesthetics
plt.figure(figsize=(16, 8))

# 1. Distribution of Units Sold
plt.subplot(2, 2, 1)
sns.histplot(df['Units Sold'], bins=15, kde=True)
plt.title('Distribution of Units Sold')

# 2. Distribution of Sales Revenue
plt.subplot(2, 2, 2)
sns.histplot(df['Sales Revenue (USD)'], bins=15, kde=True)
plt.title('Distribution of Sales Revenue')

# 3. Distribution of Discount Percentage
plt.subplot(2, 2, 3)
sns.histplot(df['Discount Percentage'], bins=10, kde=True)
plt.title('Distribution of Discount Percentage')

# 4. Distribution of Marketing Spend
plt.subplot(2, 2, 4)
sns.histplot(df['Marketing Spend (USD)'], bins=10, kde=True)
plt.title('Distribution of Marketing Spend')

plt.tight_layout()

# Display the figure with Streamlit
st.pyplot(plt)

st.title("Sales Trends and Marketing Impact Visualizations")
# Sales trend over time
plt.figure(figsize=(10, 6))
df.groupby('Date')['Sales Revenue (USD)'].sum().plot()
plt.title('Total Sales Revenue Over Time')
plt.ylabel('Sales Revenue (USD)')
plt.xlabel('Date')

# Display sales trend plot with Streamlit
st.subheader("Sales Trend Over Time")
st.pyplot(plt)

# Discount Percentage vs Sales Revenue
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Discount Percentage', y='Sales Revenue (USD)', data=df)
plt.title('Discount Percentage vs Sales Revenue')

# Display scatter plot with Streamlit
st.subheader("Discount Percentage vs Sales Revenue")
st.pyplot(plt)

# Marketing Spend vs Units Sold
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Marketing Spend (USD)', y='Units Sold', data=df)
plt.title('Marketing Spend vs Units Sold')

# Display scatter plot with Streamlit
st.subheader("Marketing Spend vs Units Sold")
st.pyplot(plt)

# Clear the figure for future plots (optional)
plt.clf()