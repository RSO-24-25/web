import os
import requests



INVOICE_SERVICE_URL = os.getenv("INVOICE_SERVICE_URL", "http://localhost:8000")


def generate_invoice(sender_name: str, receiver_name: str, amount: float) -> str:
    """
    Sends a POST request to the invoice_service to generate an invoice PDF.
    Saves the PDF locally and returns the file path.

    :param sender_name: Name of the sender for the invoice.
    :param receiver_name: Name of the receiver for the invoice.
    :param amount: The amount (float) to be included in the invoice.
    :return: Path to the saved invoice PDF file, or an empty string in case of errors.
    """

    # Construct the JSON payload according to the invoice_service's requirements
    payload = {
        "sender_name": sender_name,
        "receiver_name": receiver_name,
        "amount": amount
    }

    try:
        # Make a POST request to the /generate-invoice endpoint
        url = f"{INVOICE_SERVICE_URL}/generate-invoice"
        response = requests.post(url, json=payload, stream=True)

        if response.status_code == 200:
            # Create a filename for the invoice
            sanitized_invoice_id = f"{sender_name}_{receiver_name}_{amount}".replace(" ", "_")
            pdf_filename = f"invoice_{sanitized_invoice_id}.pdf"

            # Write the PDF to a local file

            
            # with open(pdf_filename, "wb") as pdf_file:
            #     for chunk in response.iter_content(chunk_size=8192):
            #         pdf_file.write(chunk)

            print(f"Invoice successfully generated and saved to {pdf_filename}")
            return pdf_filename
        else:
            print(f"Failed to generate invoice. Status: {response.status_code}, Response: {response.text}")
            return ""

    except Exception as e:
        print(f"Error while generating invoice: {e}")
        return ""


def get_invoice_service_status() -> str:
    """
    Simple helper to check if the invoice_service is up by calling its /status endpoint.
    Returns the status message from the invoice_service.
    """
    try:
        url = f"{INVOICE_SERVICE_URL}/status"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("status", "Unknown status")
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Exception occurred: {e}"