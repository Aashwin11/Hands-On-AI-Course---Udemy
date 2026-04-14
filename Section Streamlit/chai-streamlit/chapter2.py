# Widgets and COnditionals

import streamlit as st

st.title("Widgets and Conditionals")
st.subheader("Chai Maker App")

#Button
if st.button("Make Chai"):
    st.success("Your chai is being brewed")

#Checkbox
add_masala=st.checkbox("Add masala")
if add_masala:
    st.write("Masala added to your chai")

#Radio Button
tea_type=st.radio("Pick your chai Base: ", ["Milk","Water","Almond Milk","Honey"])
st.write(f"Selected Base :{tea_type}")


flavour=st.selectbox("Choose flavour: ",["Sweet","Ginger","Kesar","Elaichi"])
st.write(f"Selected flavour :{flavour}")

#Slider
sugar=st.slider("Sugar level", 0,5,2) # 0 - min value, 5 -max value, 2- default value
st.write(f"Selected sugar level :{sugar}")


#Uncontrolled inputs

cups=st.number_input("How many cups",min_value=1, max_value=10,step=1)
st.write(f"Selected cups :{cups}")


name=st.text_input("Enter your name")
if name:
    st.write(f"Welcome ! {name}, your chai is on way")
else:
    st.write("Cannot locate name")

dob=st.date_input("Select DOB")
st.write(f"Selected DOB: {dob}")