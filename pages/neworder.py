import streamlit as st
st.set_page_config(page_title="OIMS", page_icon="🐍")
from helper_functions import is_user_logged_in






# New Order Page
def new_order_page():
    st.title("Create a New Order")

    if not is_user_logged_in():
        st.warning("Please log in to view your orders.")
        if st.button("Login"):
            st.switch_page("pages/login.py")
        if st.button("Register"):
            st.switch_page("pages/registration.py")
        st.stop()
    
    else:
        product_name = st.text_input("Product Name", placeholder="Enter the product name")
        quantity = st.date_input("Quantity")
        # submitted = st.form_submit_button("Submit Order")
        if st.button("Back to All Orders"):
            st.switch_page("pages/my_products.py")
        if st.button("Submit Order"):
            st.switch_page("pages/my_products.py")
        # if submitted:
        #     # Logic to save the new order (e.g., write to database, session_state, etc.)
        #     st.success(f"New order for '{product_name}' created successfully!")

            # Optionally navigate back to the All Orders page

new_order_page()
