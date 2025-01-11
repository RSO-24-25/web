import streamlit as st

st.set_page_config(page_title="OIMS", page_icon="🐍")

from helper_functions import logout_user, get_username, is_user_logged_in, save_product, get_user_products, get_token, get_email

def my_products_page():
    st.title("All Orders")

    if  not is_user_logged_in():
    # if not is_user_logged_in():
        st.warning("Please log in to view your orders.")
        if st.button("Login"):
            st.switch_page("pages/login.py")
        if st.button("Register"):
            st.switch_page("pages/registration.py")
        st.stop()
    else:
        st.write(f"Welcome back, {get_username()}! Here are your orders. Click on an order to view its details:")


        # products = get_user_products(str(get_token()))
        # products = get_user_products(str(get_email()))
        print("haha")
        products = get_user_products(str(get_token()))
        # print(get_all_products())
        # response = send_token(str(get_token()))
        # if response:
        #     response_data = response.json()
        #     products = response_data['products']

        i = 0
        for product in products:
            i += 1
            print(f"{i}: {product['name']} - (Quantity: {product['quantity']} (ID: {product['id']}))")
            if st.button(f"{i}: {product['name']} - (Quantity: {product['quantity']} (ID: {product['id']}))"):
                # Store the selected order in session_state 
                save_product(product['id'])
                st.switch_page("pages/check_product.py")


        st.write("---")  # Separator
        if st.button("New Product"):
            st.switch_page("pages/new_product.py")

    if st.button("Logout"):
        logout_user()
        st.switch_page("app.py")


my_products_page()
