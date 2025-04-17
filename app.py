import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("raw.githubusercontent.com_iantonios_dsc205_refs_heads_main_bike_sharing.csv")

st.title('Bike Sharing Data Explorer')
st.write(df.head())
