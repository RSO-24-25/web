import streamlit as st

# Mock database (used for simplicity)
users_db = {}

# Registration page
def registration_page():
    st.title("Registration Page")
    username = st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")
    
    if st.button("Register"):
        if username and password:
            users_db[username] = {"password": password, "orders": []}
            st.success(f"User {username} registered successfully!")
            st.switch_page("pages/allorders.py")
        else:
            st.error("Please provide both username and password.")

registration_page()
