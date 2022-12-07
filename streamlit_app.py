import streamlit as st

st.write("""
# TDS Graded Assignment 8

App to find sum of two numbers
""")
#Get Input

st.header('Enter two numbers')
number1 = st.number_input("First Number:")
number2 = st.number_input("Second Number:")

st.write("Sum of two given numbers: ", number1, " and ", number2, " is: ", number1 + number2)
