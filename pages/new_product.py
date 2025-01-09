import streamlit as st
st.set_page_config(page_title="OIMS", page_icon="🐍")
from helper_functions import is_user_logged_in, add_product, get_email






# New Order Page
def new_product_page():
    st.title("Create a new product")

    if not is_user_logged_in():
        st.warning("Please log in to view your orders.")
        if st.button("Login"):
            st.switch_page("pages/login.py")
        if st.button("Register"):
            st.switch_page("pages/registration.py")
        st.stop()
    
    else:

        product_name = st.text_input("Product Name", placeholder="Enter the product name")
        # product_code = st.text_input("Product Code", placeholder="Enter the product code")
        product_description = st.text_input("Product Description", placeholder="Enter the product description")
        # submitted = st.form_submit_button("Submit Order")
        if st.button("Back to my products"):
            st.switch_page("pages/my_products.py")
        if st.button("Create new product"):
            print(add_product(product_name, product_description, 0, get_email()))
            st.switch_page("pages/my_products.py")

new_product_page()
