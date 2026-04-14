# Talking to data
import streamlit as st
import pandas as pd

st.title("Data talking")
st.subheader("Chai Sales Dashboard")

#take file in(or file upload)
file=st.file_uploader("Upload your csv file",type=["csv"])

if file:
    st.success("File found")
    df=pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(df)

if file:
    st.subheader("Summary stats")
    st.write(df.describe())

if file:
    Cities=df["City"].unique()
    selected_city=st.selectbox("Filter by cities",Cities)
    filtered_data=df[df["City"] == selected_city]
    st.dataframe(filtered_data)