import streamlit as st

st.set_page_config(page_title="OIMS", page_icon="🐍")

from helper_functions import logout_user, get_username, is_user_logged_in, save_product, get_all_products, get_all_users, check_mail
# Check if the user is logged in

# Simulate a list of orders with details
# orders = [
#     {"id": 1, "product": "Product A", "date": "2024-12-01"},
#     {"id": 2, "product": "Product B", "date": "2024-12-02"},
#     {"id": 3, "product": "Product C", "date": "2024-12-03"},
# ]

# Display all orders
def my_products_page():
    st.title("All Orders")

    if not is_user_logged_in():
        st.warning("Please log in to view your orders.")
        if st.button("Login"):
            st.switch_page("pages/login.py")
        if st.button("Register"):
            st.switch_page("pages/registration.py")
        st.stop()
    else:
        st.write(f"Welcome back, {get_username()}! Here are your orders. Click on an order to view its details:")
        check_mail()

        products = get_all_products()

        # pr
        i = 0
        for product in products:
            i += 1
            print(f"{i}: {product['name']} - (Quantity: {product['quantity']} (ID: {product['_id']}))")
            if st.button(f"{i}: {product['name']} - (Quantity: {product['quantity']} (ID: {product['_id']}))"):
                # Store the selected order in session_state
                save_product(product['_id'])
                st.switch_page("pages/check_product.py")


        st.write("---")  # Separator
        if st.button("New Product"):
            st.switch_page("pages/new_product.py")

        if st.button("Logout"):
            logout_user()
            st.switch_page("app.py")


my_products_page()
