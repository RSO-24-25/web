import streamlit as st

# Check if the user is logged in
def check_login():
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        st.warning("Please log in to view your orders.")
        st.stop()

# Simulate a list of orders with details
orders = [
    {"id": 1, "product": "Product A", "date": "2024-12-01"},
    {"id": 2, "product": "Product B", "date": "2024-12-02"},
    {"id": 3, "product": "Product C", "date": "2024-12-03"},
]

# Display all orders
def all_orders_page():
    st.title("All Orders")

    # Check login status
    # check_login()

    st.write("Here are your orders. Click on an order to view its details:")

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

all_orders_page()
