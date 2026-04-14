import streamlit as st


st.title("Hello Chai App")
st.subheader("Brewed with Streamlit")
st.text("Welcome to your 1st interactive app")
st.write("Choose your favourite variety of chai")

chai=st.selectbox("Your fav chai:",["masala chai","lemon chai","ginger tea"])
st.write(f"You choose {chai}. Excellent choice")

st.success("Your chai has been brewed")

# Widgets and COnditionals
