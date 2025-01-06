import streamlit as st
st.set_page_config(page_title="OIMS", page_icon="🐍")
from helper_functions import is_user_logged_in




# Display details of a specific order
def check_order_page():
    st.title("Order Details")

    if not is_user_logged_in():
        st.warning("Please log in to view your orders.")
        # st.stop()
        if st.button("Login"):
            st.switch_page("pages/login.py")
        if st.button("Register"):
            st.switch_page("pages/registration.py")
        st.stop()
    else:


        # Check if an order is selected
        if "selected_order" not in st.session_state:
            st.error("No order selected. Please go back to the All Orders page.")
            st.stop()

        # Retrieve the selected order details from session_state
        order = st.session_state.selected_order

        # Display the order details
        st.write(f"**Order ID**: {order['id']}")
        st.write(f"**Product**: {order['product']}")
        st.write(f"**Order Date**: {order['date']}")

        # Add a button to go back to the All Orders page
        if st.button("Back to All Orders"):
            st.switch_page("pages/allorders.py")

check_order_page()
