# === Streamlit Calculator ===

import streamlit as st

st.set_page_config(page_title="SKDC Loader Volume-Driven Annual Savings Calculator", layout="wide")

st.image("Ambitions Public Sector Logo.png", width=240)
st.markdown(
    "<h1 style='font-size: 40px;'>SKDC Loader Volume-Driven Annual Savings Calculator</h1>",
    unsafe_allow_html=True
)

fixed_number = 9436.24

user_input = st.number_input(
  "Enter the quantity of workers", min_value=1, step=1, format="%d")

result = user_input * fixed_number

formatted_result = f"£{result:,.2f}"

st.markdown(
    f"""
    <p style='font-size:40px; font-weight:bold; text-align:center;'>
        Annual Savings Achieved: {formatted_result}
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("<p style='color: red;'>Annual Savings Achieved: {formatted_result}</p>", unsafe_allow_html=True)



