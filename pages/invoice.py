import streamlit as st
from invoice_helper import generate_invoice, get_invoice_service_status

def run_invoice_app():
    """
    This function contains all the Streamlit UI code and can be called from main
    or any other place in your code.
    """
    st.title("Invoice Generator")

    if st.button("Check Invoice Service Status"):
        status = get_invoice_service_status()
        st.write(f"Invoice Service Status: {status}")

    sender_name = st.text_input("Sender Name")
    receiver_name = st.text_input("Receiver Name")
    amount = st.number_input("Amount", min_value=0.0)

    if st.button("Generate Invoice"):
        pdf_path = generate_invoice(sender_name, receiver_name, amount)
        if pdf_path:
            st.success(f"Invoice generated: {pdf_path}")

            # Optionally, offer a download button
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="Download Invoice",
                    data=f,
                    file_name=pdf_path,
                    mime="application/pdf"
                )
        else:
            st.error("Failed to generate invoice.")


if __name__ == "__main__":
    run_invoice_app()