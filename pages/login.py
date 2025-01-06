import streamlit as st
st.set_page_config(page_title="Login to OIMS", page_icon="🐍")
from helper_functions import user_log_in





# Login page
def login_page():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    col1, col2 = st.columns([8, 1])

    with col1:
        if st.button("Back"):
            st.switch_page("app.py")

    with col2:
        if st.button("Log In"):
            if username and password:
                if user_log_in(username, password):
                    st.success(f"Welcome back, {username}!")
                    st.switch_page("pages/allorders.py")
                else:
                    st.error(f"Login failed")
            else:
                st.error("Please provide both username and password.")

login_page()
