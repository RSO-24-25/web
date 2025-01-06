import streamlit as st
from helper_functions import logout_user, get_username, is_user_logged_in

# st.set_page_config(page_title="OIMS", page_icon="🐍")

# Check if the user is logged in

# Simulate a list of orders with details
orders = [
    {"id": 1, "product": "Product A", "date": "2024-12-01"},
    {"id": 2, "product": "Product B", "date": "2024-12-02"},
    {"id": 3, "product": "Product C", "date": "2024-12-03"},
]

# Display all orders
def all_orders_page():
    st.title("All Orders")

    if not is_user_logged_in():
        st.warning("Please log in to view your orders.")
        # st.stop()
        if st.button("Login"):
            st.switch_page("pages/login.py")
        if st.button("Register"):
            st.switch_page("pages/registration.py")
        st.stop()
    else:
        st.write(f"Welcome back, {get_username()}! Here are your orders. Click on an order to view its details:")

        # Display each order as a button
        for order in orders:
            if st.button(f"Order {order['id']} - {order['product']} (Date: {order['date']})"):
                # Store the selected order in session_state
                st.session_state.selected_order = order
                # Navigate to the specific order page
                st.switch_page("pages/checkorder.py")

        # Add a button for creating a new order
        st.write("---")  # Separator
        if st.button("New Order"):
            st.switch_page("pages/neworder.py")

        if st.button("Logout"):
            logout_user()
            st.switch_page("app.py")

all_orders_page()
