import streamlit as st
st.set_page_config(page_title="OIMS", page_icon="🐍")
from helper_functions import is_user_logged_in






# New Order Page
def new_order_page():
    st.title("Create a New Order")

    if not is_user_logged_in():
        st.warning("Please log in to view your orders.")
        # st.stop()
        if st.button("Login"):
            st.switch_page("pages/login.py")
        if st.button("Register"):
            st.switch_page("pages/registration.py")
        st.stop()
    
    else:

        # Form for creating a new order
    # with st.form("new_order_form"):
        product_name = st.text_input("Product Name", placeholder="Enter the product name")
        order_date = st.date_input("Order Date")
        # submitted = st.form_submit_button("Submit Order")
        if st.button("Back to All Orders"):
            st.switch_page("pages/allorders.py")
        if st.button("Submit Order"):
            st.switch_page("pages/allorders.py")
        # if submitted:
        #     # Logic to save the new order (e.g., write to database, session_state, etc.)
        #     st.success(f"New order for '{product_name}' created successfully!")

            # Optionally navigate back to the All Orders page

new_order_page()
