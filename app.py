import streamlit as st
st.set_page_config(page_title="OIMS", page_icon="🐍")#, initial_sidebar_state="collapsed")
from streamlit_cookies_manager import EncryptedCookieManager


from helper_functions import is_user_logged_in, get_username, get_weather



st.title("Welcome to OIMS!")

try:
    weather = get_weather()
    temp_k = weather["main"]["temp"]  # Temperature in Kelvin
    temp_c = round(temp_k - 273.15)
    basic = weather["weather"][0]["main"]
    description = f"Weather in Ljubljana: {basic}, {temp_c} °C"
except:
    description = "Weather info not availibe!"


st.write(description)

if is_user_logged_in():
    
    st.write(f"Welcome back, {get_username}!")
    st.write("You can check your orders now!")
    st.write("---") 
    st.page_link(label="Check orders", page="pages/allorders.py") 
else:
    st.write("You are not logged in.")
    st.write("Please log in or register to access the features.")
    st.write("---")
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col2:
        if st.button("Login"):
            st.switch_page("pages/login.py")

    with col5:
        if st.button("Register"):
            st.switch_page("pages/registration.py")
