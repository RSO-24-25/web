import streamlit as st

# New Order Page
def new_order_page():
    st.title("Create a New Order")

    # Form for creating a new order
    with st.form("new_order_form"):
        product_name = st.text_input("Product Name", placeholder="Enter the product name")
        order_date = st.date_input("Order Date")
        submitted = st.form_submit_button("Submit Order")

        if submitted:
            # Logic to save the new order (e.g., write to database, session_state, etc.)
            st.success(f"New order for '{product_name}' created successfully!")

            # Optionally navigate back to the All Orders page
            if st.button("Back to All Orders"):
                st.switch_page("pages/allorders.py")

new_order_page()
