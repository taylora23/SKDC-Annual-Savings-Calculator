# === Streamlit Calculator ===

import streamlit as st

st.set_page_config(page_title="SKDC Loader Volume-Driven Annual Savings Calculator", layout="wide")

st.title("SKDC Loader Volume-Driven Annual Savings Calculator")
st.image("Ambitions Public Sector Logo.png", width=120)

fixed_number = 9436.24

user_input = st.number_input(
  "Enter a number", min_value=1, step=1, format="%d")

result = user_input * fixed_number

formatted_result = f"£{result:,.2f}"

st.write(f"Result: {user_input} x £{fixed_number:,.2f} = {formatted_result}")



