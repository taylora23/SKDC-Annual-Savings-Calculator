# === Streamlit Calculator ===

import streamlit as st

st.title("SKDC Loader Volume-Driven Annual Savings Calculator")

fixed_number = 9436.24

user_input = st.number_input("Enter a number")

result = user_input * fixed_number


st.write(f"Result: {user_input} x {fixed_number} = {result}")
