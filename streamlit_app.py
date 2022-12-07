import streamlit as st

st.write("""
# Credit Card Approval Prediction App

This app predicts the credit card approval probablity
""")
#Get Input

st.header('User Input Parameters')
number1 = st.number_input("Number1",min_value=0,max_value=20,step=1)
number2 = st.number_input("Number2",min_value=0,max_value=20,step=1)

st.write("Sum of two numbers: ", number1, " and ", number2, "is:", number1 + number2)
