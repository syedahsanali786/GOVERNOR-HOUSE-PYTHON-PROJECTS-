import streamlit as st

def check_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Medium"
    else:
        return "Strong"

st.title("Login & Password Strength Checker")

# User Input
username = st.text_input("Enter your username:")
password = st.text_input("Enter your password:", type="password")

# Check Login and Password Strength
if username and password:
    strength = check_strength(password)
    st.write(f"Hello, **{username}**! Your password strength is: **{strength}**")
