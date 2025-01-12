import streamlit as st
import grpc
import service_pb2
import service_pb2_grpc
from PIL import Image
from io import BytesIO
from streamlit_cookies_manager import EncryptedCookieManager

cookies = EncryptedCookieManager(
    prefix="oims_",
    password="YourSecurePassword"
)


if not cookies.ready():
    st.stop()

def save_stat_prod(id):
    cookies["stat_product"] = str(id)

def get_stat_prod():
    return cookies["stat_product"]


def get_prices_graph(id):
# Connect to the gRPC server
    channel = grpc.insecure_channel('statistics-service:50052')
    stub = service_pb2_grpc.StatisticsStub(channel)
    id = str(id)
    # Request the plot image
    response = stub.Get_Prices_Graph(service_pb2.HelloRequest(id=id))

    # Convert the byte stream to an image
    image_data = response.image
    image = Image.open(BytesIO(image_data))
    return image

# # Display the image
# image.show()




def get_availible_products():
    channel = grpc.insecure_channel('statistics-service:50052')
    stub = service_pb2_grpc.StatisticsStub(channel)

    # Create a request object (we don't need to send anything in the request for Get_all_products)
    request = service_pb2.HelloRequest(id="client")

    # Call the Get_all_products method
    response = stub.Get_all_products(request)
    return response.products
    # Print the result (a list of products)
    # print("All Products:")
    # for product in response.products:
    #     print(f"ID: {product.id}, Name: {product.name}")



# Optionally, save the image
# image.save("price_plot.png")
