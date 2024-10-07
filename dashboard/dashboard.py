import streamlit as st
import pandas as pd
import os 
import matplotlib.pyplot as plt
import seaborn as sns

script_dir = os.path.dirname(__file__)
dongsi_path = os.path.join(script_dir, 'dongsi.csv')

def load_data():
    data = pd.read_csv(dongsi_path)
    return data

# Load the data
data = load_data()

# Title of the dashboard
st.title("Air Quality Analysis Dashboard")

# Display the raw data (optional)
if st.checkbox("Show Raw Data"):
    st.write(data)

# Visualize Wind Speed trends in April to May for Dongsi
st.header("Wind Speed Trends - Dongsi District")
plt.figure(figsize=(10, 5))
sns.lineplot(x=data['month'], y=data['WSPM'], hue=data['year'], palette='Set1')
st.pyplot(plt)

# Correlation between Temperature and polutan
st.header("Correlation between Temperature and Polutans")
plt.figure(figsize=(10, 5))
correlation_temp = data[['TEMP', 'PM25', 'PM10', 'NO2', 'SO2', 'O3']].corr()
sns.heatmap(correlation_temp, annot=True)
plt.title('Correlation between Temperature and Polutans at Dongsi Station')
st.pyplot(plt)

# Correlation between Wind Speed (WSPM) and Polutans
st.header("Correlation between Wind Speed (WSPM) and Polutans")
plt.figure(figsize=(10, 5))
correlation_wspm = data[['WSPM', 'PM25', 'PM10', 'NO2', 'SO2', 'O3']].corr()
sns.heatmap(correlation_wspm, annot=True)
plt.title('Correlation between Wind Speed and Polutans at Dongsi Station')
st.pyplot(plt)

# Display correlation heatmap for pollutants
st.header("Pollutant Correlation Heatmap")
correlation_pollutants = data[['PM25', 'PM10', 'NO2', 'SO2', 'O3']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_pollutants, annot=True)
plt.title("Correlation Matrix of Pollutants")
st.pyplot(plt)

# Display key insights
st.write("### Key Insights")
st.write('''
- Wind speed tends to be higher in Dongsi during April and May.
- There is a moderate positive correlation between temperature and O3 concentration.
- A weak positive correlation is observed between wind speed and O3 concentration.
- PM2.5 and PM10 show a strong positive correlation, while O3 has negative correlations with other pollutants.
''')


st.caption('Copyright (C) Dina Lestari. 2024')