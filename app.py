import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns
import pickle

with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
    
df = pd.read_csv('data_train.csv')

df['IPS'].unique()

st.title("Laptop Price Predictor")

company = st.selectbox('Brand', df)