import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
import requests
import time
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

# URL = "http://localhost:8000"
# URL = "http://web-auth:8000"
AUTH_URL = os.getenv("AUTHENTICATION_URL")
INV_URL_GQL = os.getenv("INVENTORY_URL")


cookies = EncryptedCookieManager(
    prefix="oims_",
    password="YourSecurePassword"
)


if not cookies.ready():
    st.stop()


def register_user(data):
    try:
        response = requests.post(AUTH_URL + "/register", json=data)

        if response.status_code == 200:
            time.sleep(1)
            user_log_in(data["username"], data["password"])
            return True, None
        else:
            return False, response.text 

    except Exception as e:
        return False, str(e)




def user_log_in(username, password):
    try:

        payload = {
            "username": username,
            "password": password
        }
        # print(payload)
        response = requests.post(AUTH_URL+"/token", data=payload, headers={"accept": "application/json"})
        # print(response)
        if response.status_code == 200:
            print("login ok!")
            token_data = response.json()
            cookies["username"] = username
            cookies["access_token"] = token_data["access_token"]
            cookies["refresh_token"] = token_data["refresh_token"]
            # user = get_token_owner_data()
            cookies["first_name"] = get_token_owner_data()['given_name']
            cookies["email"] = get_token_owner_data()["email"]
            print("saving_cookies")
            cookies.save()
            print("cookies saved!")
            # print(cookies)
            return True
        else:
            return False

    except Exception as e:
        False




def is_user_logged_in ():
    try:
        cookie = cookies["access_token"]
    except:
        cookie = ""
    # print("USER ACCES TOKEN")
    # print(cookies["access_token"])
    if cookie != "":
        return True
    else:
        return False

def get_first_name():
    return cookies["first_name"]

def get_email():
    return cookies["email"]

def get_username():
    return cookies["username"]

def get_token():
    return cookies["access_token"]

def logout_user():
    refresh_token = cookies["refresh_token"]
    cookies["access_token"] = ""  # Store token in cookie
    cookies["refresh_token"] = "" 
    cookies["username"] = ""  # Store token in cookie
    cookies["email"] = ""
    cookies["first_name"] = ""
    # cookies.save()
    forget_current_product()

    payload = {
            "refresh_token": refresh_token,
        }
    try:
        requests.post(AUTH_URL+"/logout", data=payload, headers={"accept": "application/json"})
    except Exception as e:
        print(e)



    # Overwrite the cookies with an empty value and set them to expire in the past
    




def get_token_owner_data():
    url = AUTH_URL + "/user-info"
    headers = {"Authorization": f"Bearer {get_token()}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  

        user_info = response.json()

        print(user_info)
        return user_info
    except:
        return None



def get_weather():

    city = "Ljubljana"
    # api_key = "bfb8dccd0b442d975ff062d1f67e9ec8"
    api_key = os.getenv("WEATHER_API_KEY")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    # Send a request to the API
    response = requests.get(url)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Error: {response.status_code}"



def get_top_headlines():
    # api_key = "c061ba6443df4b2997b094811d29c11e"
    api_key = os.getenv("NEWS_API_KEY")
    country = "us"
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    
    # Make a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract articles
        articles = data.get("articles", [])
        headlines = []
        for article in articles:
            headlines.append(article["title"])
        
        return headlines
    else:
        return f"Error: {response.status_code} - {response.reason}"
    

# MONGO_URI="mongodb+srv://mongodb:galjetaksef123!@mongoloidgal.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
# client = MongoClient(MONGO_URI)
# db = client.inventory_db  # Replace with your database name
# users_collection = db.users  # Replace with your users collection name
# products_collection = db.products  # Replace with your products collection name

def add_product(name, description, quantity, owner_email):
    mutation = f"""
    mutation {{
        createProduct(name: "{name}", description: "{description}", quantity: {quantity}, ownerEmail: "{owner_email}") {{
            product {{
                id
                name
                description
                quantity
                ownerEmail
            }}
        }}
    }}
    """

    # Set headers (include authentication if needed)
    headers = {
        "Content-Type": "application/json",
        # Add your token if required
        # "Authorization": f"Bearer {your_token}"
    }

    # Send the request
    response = requests.post(INV_URL_GQL, json={"query": mutation}, headers=headers)
    data = response.json()
    print(data)
    # if 'errors' in data:
    #     print(f"Error: {data['errors']}")




def get_user_products(token):

    print(token[:10])

    # GraphQL query with variables
    # token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJLdjRVRzdSRUx6c3p0aFQwU1A3cGlGVXY1TlZNTnF2NWdqSDVHcFNYajRVIn0.eyJleHAiOjE3MzY1NDU3NjIsImlhdCI6MTczNjU0MjE2MiwianRpIjoiMjFkMTIwZTEtNGEwMy00NmJjLTkzMjEtMjE5MTVkZGU2YzFkIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL215cmVhbG0iLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMDJhODRhYzAtMGZiZS00OTk5LTlhZTYtYmVmOGJmZTczYzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoibXljbGllbnQiLCJzaWQiOiIyZTg2ZWVkYS01NTk2LTRjYTktODk1ZC1mNGJjMDI1ODA0ZGEiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtbXlyZWFsbSIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iLCJ1c2VyIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsibXljbGllbnQiOnsicm9sZXMiOlsic2VmZ2FsIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBlbWFpbCBwcm9maWxlIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoiR2FsIE1lbmHFoWUiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJnYWxrbzEyMyIsImdpdmVuX25hbWUiOiJHYWwiLCJmYW1pbHlfbmFtZSI6Ik1lbmHFoWUiLCJlbWFpbCI6ImdhbGtvLm1lbmFzZUBnbWFpbC5jb20ifQ.or_PNtnUlU8Wxbexy8ATlX6MJO8eKYe9DZ7qFBXZ_avzWno-u6P-TEj1yTt3sRdduFGCpSizVh9gb7FH9gwUNh1YE5I39ltmoKwJPWJ5cafPXNBj-byacb7ZeUxTmdQPZBggeoxBLTryN6drb71miAS7pMCaOrfCdyWcZ7Qwd6MTcMAg0OrlhS-1TJf1KYb585ocwh-_bOdYabaIWPjaFU2dv5hR9imOMIAW1o_OGwYAVSfZWTpP-YUZEOKah1A68wYpEswaCYup7vAZmTv9isD-rQfXKnCpcg_KKBEI4qZuOUGzoIvBiWp65_apOVsSTeQo-zkB1ynL54oLXiXOhg"
    query = f"""
    query {{
        productsByToken(token: "{token}") {{
            id
            name
            description
            quantity
            ownerEmail
        }}
    }}
    """   
    headers = {
        "Content-Type": "application/json"
    }
    
    # Make the request
    response = requests.post(INV_URL_GQL, json={"query": query}, headers=headers)
    # response = requests.post(INV_URL_GQL, json={"query": query, "variables": variables})
    data = response.json()
    print(data)
    products = data.get('productsByToken', [])
    # print(products)
    return  products


def is_user_in_the_database(email):
    query = f"""
    {{
    userByEmail(email: "{email}") {{
        id
        email
    }}
    }}
    """
    response = requests.post(INV_URL_GQL, json={'query': query})
    data = response.json()
    if (data['userByEmail']):
        print("Mail exists!")
    else: 
        print("Mail does not exist, adding it to the base!")

        mutation = f"""
        mutation {{
        createUser(email: "{email}") {{
            user {{
            id
            email
            }}
        }}
        }}
        """
        response = requests.post(INV_URL_GQL, json={'query': mutation})
        if response.status_code == 200:
            print("Mail succesfully added")
        else:
            print(f"Error {response.status_code}: {response.text}")

       


def delete_product(product_id):

    mutation = f"""
    mutation {{
        deleteProduct(id: "{product_id}") {{
            success
        }}
    }}
    """

    # Set headers (include authentication if needed)
    headers = {
        "Content-Type": "application/json",
        # Add your token if required
        # "Authorization": f"Bearer {your_token}"
    }

    # Send the request
    response = requests.post(INV_URL_GQL, json={"query": mutation}, headers=headers)

    # Parse the response
    data = response.json()
    print(data)
    



def update_product_quantity(product_id, new_quantity):
    mutation = f"""
    mutation {{
        updateProductQuantity(id: "{product_id}", quantity: {new_quantity}) {{
            product {{
                id
                name
                description
                quantity
                ownerEmail
            }}
        }}
    }}
    """
    print(f"new {new_quantity}")
    variables = {
        "id": str(product_id),
        "quantity": float(new_quantity)
    }

    headers = {
        "Content-Type": "application/json",
        # Add authentication headers if required
    }

    response = requests.post(INV_URL_GQL, json={"query": mutation, "variables": variables}, headers=headers)


    # Parse the response
    data = response.json()
    print(data)

    # # Check if there are any errors
    # if 'errors' in data:
    #     print(f"Error: {data['errors']}")
    # else:
    #     # Get the response data
    #     updated_product = data.get('data', {}).get('updateProductQuantity', None)
    #     if updated_product:
    #         print(f"Product quantity updated: {updated_product['name']} (ID: {updated_product['id']}, Quantity: {updated_product['quantity']})")
    #     else:
    #         print(f"Product with ID {product_id} not found or could not be updated.")



def save_product(product):
    cookies["product"] = product
    cookies.save()

def get_current_product():
    return cookies["product"]

def forget_current_product():
    cookies["product"] = ""
    cookies.save()


def get_product_by_id(product_id):

    query = """
    {
      productById(id: "%s") {
        id
        description
        name
        quantity
        ownerEmail
      }
    }
    """ % product_id  # Insert the product_id dynamically

    # Prepare the payload
    payload = {
        'query': query
    }

    # Send the POST request to the GraphQL server
    response = requests.post(INV_URL_GQL, json=payload)
    # print(response)
    # Parse the response
    if response.status_code == 200:
        data = response.json()
        print(data)
        # Return the product data if available
        if 'productById' in data:
            return data['productById']
        else:
            return {"error": "Product not found or invalid ID"}
    else:
        return {"error": f"Error {response.status_code}: {response.text}"}




# def send_token(token):
#     payload = {
#         "token": token
#     }
    
#     response = requests.post(INV_URL + "/post-token", json=payload)
#     print(response)
#     # Check the response
#     if response.status_code == 200:
#         print("Success")
#         # print("Token received successfully:", response.json())
#         return response
#     else:
#         # print("Error:", response.json())
#         print("Error")
#         return None

