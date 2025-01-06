import streamlit as st
import time
st.set_page_config(page_title="Register to OIMS", page_icon="🐍")

from helper_functions import register_user



users_db = {}

def registration_page():
    st.title("Registration Page")

    email = st.text_input("Enter your e-mail")
    firstName = st.text_input("Enter your first name")
    lastName = st.text_input("Enter your last name")
    username = st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")

    col1, col2 = st.columns([7, 1])

    with col1:
        if st.button("Back"):
            st.switch_page("app.py")
    
    with col2:
        if st.button("Register"):
            if username and password and email and firstName and lastName:
                data = {
                    "email": email,
                    "username": username,
                    "firstName": firstName,
                    "lastName": lastName,
                    "password": password
                }

                success, error_message = register_user(data=data)
                
                if success:
                    st.success(f"User {data['username']} registered successfully!")
                    time.sleep(1)
                    st.switch_page("pages/allorders.py")
                else:
                    st.error(f"Registration failed: {error_message}")  # Display detailed error message
            else:
                st.error("All fields are required.")
                
    
registration_page()
