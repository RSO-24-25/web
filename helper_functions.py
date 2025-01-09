import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
import requests
import time
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

# URL = "http://localhost:8000"
# URL = "http://web-auth:8000"
URL = os.getenv("AUTHENTICATION_URL")


cookies = EncryptedCookieManager(
    prefix="oims_",
    password="YourSecurePassword"
)



if not cookies.ready():
    st.stop()


def register_user(data):
    try:
        response = requests.post(URL + "/register", json=data)

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
    
        response = requests.post(URL+"/token", data=payload, headers={"accept": "application/json"})
        if response.status_code == 200:
            token_data = response.json()
            cookies["username"] = username
            cookies["access_token"] = token_data["access_token"]
            cookies["email"] = get_token_owner_data()["email"]
            cookies.save()
            print(cookies)
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

    if cookie != "":
        return True
    else:
        return False

def get_email():
    return cookies["email"]

def get_username():
    return cookies["username"]

def get_token():
    return cookies["access_token"]

def logout_user():
    # Overwrite the cookies with an empty value and set them to expire in the past
    cookies["access_token"] = ""  # Store token in cookie
    cookies["username"] = ""  # Store token in cookie
    cookies["email"] = ""
    cookies.save()
    forget_current_product()




def get_token_owner_data():
    url = URL + "/user-info"
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
    

MONGO_URI="mongodb+srv://mongodb:galjetaksef123!@mongoloidgal.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
client = MongoClient(MONGO_URI)
db = client.inventory_db  # Replace with your database name
users_collection = db.users  # Replace with your users collection name
products_collection = db.products  # Replace with your products collection name

def add_product(name, description, quantity, owner_email):
    """Adds a new product to the MongoDB database."""
    
    # Check if the owner email exists in the users collection
    if not users_collection.find_one({"email": owner_email}):
        return {"error": "Owner email does not exist."}
    
    # Prepare the product data to be inserted
    product = {
        "name": name,
        "description": description,
        "quantity": quantity,
        "owner_email": owner_email
    }
    
    # Insert the product into the products collection
    result = products_collection.insert_one(product)
    
    # Return the inserted product ID
    return {"message": "Product added successfully", "product_id": str(result.inserted_id)}

def get_all_products():
    """Fetches all products from the MongoDB database."""
    # Fetch all products from the 'products' collection
    products = list(products_collection.find())  # Using find() to get all products
    # Serialize ObjectId to string for display purposes
    print(products)
    for product in products:
        product["_id"] = str(product["_id"])
    return products

def get_all_users():
    """Fetches all users from the MongoDB users collection."""
    # Fetch all users from the 'users' collection
    users = list(users_collection.find())  # Using find() to get all users
    # Serialize ObjectId to string for display purposes
    for user in users:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string for easier usage
    return users


def create_user(email):
    """Creates a new user in the MongoDB users collection."""
    
    # Check if the email already exists in the database
    if users_collection.find_one({"email": email}):
        return {"error": "Email already exists."}
    
    # Prepare the new user document
    user = {
        "email": email,
    }
    
    # Insert the new user into the users collection
    result = users_collection.insert_one(user)
    
    # Return success message and the new user's ID
    return {"message": "User created successfully", "user_id": str(result.inserted_id)}

def check_mail():
    user_email = get_email()
    users = get_all_users()

    mail_exists = False
    for user in users:
        if user["email"] == user_email:
            mail_exists = True
            print("Mail exists!")

    if not mail_exists:
        print(f"Mail does not exist! New mail created: {user_email}")
        print(create_user(user_email))
    


def delete_product(product_id):

    try:
        # Convert the product_id to an ObjectId
        object_id = ObjectId(product_id)
    except Exception as e:
        return {"error": f"Invalid product ID: {str(e)}"}
    
    # Check if the product exists
    product = products_collection.find_one({"_id": object_id})
    if not product:
        return {"error": "Product not found."}
    
    # Delete the product
    result = products_collection.delete_one({"_id": object_id})
    if result.deleted_count == 1:
        return {"message": "Product deleted successfully."}
    else:
        return {"error": "Failed to delete product."}
    



def update_product_quantity(product_id, quantity_change):
    try:
        object_id = ObjectId(product_id)
    except Exception as e:
        return {"error": f"Invalid product ID: {str(e)}"}
    
    # Find the product by its ID
    product = products_collection.find_one({"_id": object_id})
    if not product:
        return {"error": "Product not found."}
    
    # Calculate the new quantity
    new_quantity = product.get("quantity", 0) + quantity_change
    if new_quantity < 0:
        return {"error": "Quantity cannot be negative."}
    
    # Update the quantity in the database
    result = products_collection.update_one(
        {"_id": object_id},
        {"$set": {"quantity": new_quantity}}
    )
    if result.modified_count == 1:
        return {"message": "Product quantity updated successfully.", "new_quantity": new_quantity}
    else:
        return {"error": "Failed to update product quantity."}



def save_product(product):
    cookies["product"] = product
    cookies.save()

def get_current_product():
    return cookies["product"]

def forget_current_product():
    cookies["product"] = ""
    cookies.save()


def get_product_by_id(product_id):

    try:
        # Convert the product_id to an ObjectId
        object_id = ObjectId(product_id)
    except Exception as e:
        return {"error": f"Invalid product ID: {str(e)}"}
    
    # Fetch the product from the database
    product = products_collection.find_one({"_id": object_id})
    if not product:
        return {"error": "Product not found."}
    
    # Serialize the ObjectId to a string for JSON compatibility
    product["_id"] = str(product["_id"])
    return product