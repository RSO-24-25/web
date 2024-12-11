import streamlit as st

# Set the page title and icon for the app
st.set_page_config(page_title="My Multi-Page App", page_icon="🏠", initial_sidebar_state="collapsed")

# Title for the home page
st.title("Welcome to the Streamlit App!")

# Check if user is logged in
if "username" in st.session_state:
    username = st.session_state["username"]
    st.write(f"Welcome back, {username}!")
    st.write("You are logged in. Go to the Orders page or add a new order.")
else:
    st.write("You are not logged in.")
    st.write("Please log in or register to access the features.")
    st.page_link(label="Login", page="pages/login.py") 
    st.page_link(label="Register", page="pages/registration.py")

# Navigation links are automatically added to the sidebar if pages are placed in the `pages/` directory.
