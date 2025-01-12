import grpc
import streamlit as st
import os
import sys

st.set_page_config(page_title="OIMS", page_icon="🐍")
from helper_functions import is_user_logged_in, delete_product, update_product_quantity, get_current_product, get_product_by_id, get_email, get_first_name

# Import the gRPC email service files
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import email_pb2
import email_pb2_grpc

def send_email_notification(recipient_email, subject, message):
    try:
        # Connect to the gRPC server
        channel = grpc.insecure_channel('notification:50051')
        stub = email_pb2_grpc.EmailServiceStub(channel)

        # Send the email
        response = stub.SendEmail(email_pb2.EmailRequest(
            recipient_email=recipient_email,
            subject=subject,
            message=message
        ))
        return response.status
    except Exception as e:
        return f"Error: {e}"


# Display details of a specific order
def check_product_page():
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

        # Retrieve the selected order details from session_state
        product = get_product_by_id(get_current_product())
        # product = get_product_by_id("677ec87bc706e6174ce25a60")
        print(product)
        if product == "":
            st.error("No order selected. Please go back to the All Orders page.")
            st.stop()

        # Display the order details
        st.write(f"**Product Name**: {product['name']}")
        st.write(f"**Product ID**: {product['id']}")
        st.write(f"**Product Description**: {product['description']}")
        st.write(f"**Product Quantity**: {product['quantity']}")
        st.write(f"**Product Owner**: {product['ownerEmail']}")

        buy_quantity = st.number_input("Buy quantity", placeholder="Enter how much you want to buy")
        if st.button("Buy product"):
            print(update_product_quantity(product['id'], product['quantity'] + buy_quantity))
            # send_email_notification(get_email(), "Izdelki uspešno kupljeni!" f"Pozdravljeni {get_first_name()}\n\n uspešno ste kupili izdelek {product['name']} (količina: {buy_quantity}).\n\nLep pozdrav,\n\nEkipa OIMS")
            st.switch_page("pages/check_product.py")

        sell_quantity = st.number_input("Sell quantity", placeholder="Enter how much you want to sell")
        if st.button("Sell product"):
            print(update_product_quantity(product['id'], product['quantity']-sell_quantity))
            # send_email_notification(get_email(), "Izdelki uspešno kupljeni!" f"Pozdravljeni {get_first_name()}\n\n uspešno ste prodali izdelek {product['name']} (količina: {sell_quantity}).\n\nLep pozdrav,\n\nEkipa OIMS")
            st.switch_page("pages/check_product.py")


        # Add a button to go back to the All Orders page
        if st.button("Delete this product"):
            delete_product(product['id'])
            st.switch_page("pages/my_products.py")

        if st.button("Back to my products"):
            st.switch_page("pages/my_products.py")


            


check_product_page()
