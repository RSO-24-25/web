import grpc
import streamlit as st
import os
import sys

st.set_page_config(page_title="OIMS", page_icon="🐍")

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

def notification_page():
    st.title("Send Notifications")

    # Input fields for the notification
    recipient_email = st.text_input("Recipient Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message")

    if st.button("Send Notification"):
        if not recipient_email or not subject or not message:
            st.error("All fields are required.")
        else:
            status = send_email_notification(recipient_email, subject, message)
            if status == "Email sent successfully!":
                st.success("Notification sent successfully!")
            else:
                st.error(f"Failed to send notification. {status}")

# Display the page
notification_page()
