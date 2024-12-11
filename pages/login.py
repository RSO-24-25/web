import streamlit as st

# Mock database (used for simplicity)
users_db = {
    "user1": {"password": "123", "orders": []},
    "user2": {"password": "password456", "orders": []}
}

# Function to authenticate the user
def authenticate_user(username, password):
    if username in users_db and users_db[username]["password"] == password:
        return True
    return False

# Login page
def login_page():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Log In"):
        if authenticate_user(username, password):
            st.session_state["username"] = username
            st.success(f"Welcome back, {username}!")
            st.switch_page("pages/allorders.py")
        else:
            st.error("Invalid username or password.")

login_page()
