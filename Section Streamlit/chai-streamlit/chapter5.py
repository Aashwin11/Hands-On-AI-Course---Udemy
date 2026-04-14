#Web requests and API calls
#API Web URL: https://v6.exchangerate-api.com/v6/9fea989e89a322fef0255352/latest/INR

import streamlit as st
import requests

st.title("Web Requests and API call")
amount=st.number_input("Enter the amount in INR", min_value=1,max_value=1000)

target_currency=st.selectbox("Convert to:", ["USD", "EUR", "GBP","YEN"])

if st.button("Convert"):
    url="https://v6.exchangerate-api.com/v6/9fea989e89a322fef0255352/latest/INR"
    response=requests.get(url)
    if response.status_code ==200:
        data=response.json()
        target_currency_value=data["conversion_rates"][target_currency]
        converted=target_currency_value*amount
        st.success(f"{amount}INR = {converted:.2f}{target_currency}")
    else:
        st.error("Request failed to fetch conversion rate")
