import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
import requests
import time

URL = "http://localhost:8000"

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


def get_username():
    return cookies["username"]

def logout_user():
    # Overwrite the cookies with an empty value and set them to expire in the past
    cookies["access_token"] = ""  # Store token in cookie
    cookies["username"] = ""  # Store token in cookie
    cookies.save()




def get_weather():

    city = "Ljubljana"
    api_key = "bfb8dccd0b442d975ff062d1f67e9ec8"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    # Send a request to the API
    response = requests.get(url)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Error: {response.status_code}"