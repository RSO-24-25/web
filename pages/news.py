import streamlit as st
st.set_page_config(page_title="News", page_icon="🐍")
from helper_functions import get_weather, get_top_headlines





# Login page
def news_page():

    st.title("Weather and News")
    
    try:
        weather = get_weather()
        temp_k = weather["main"]["temp"]  # Temperature in Kelvin
        temp_c = round(temp_k - 273.15)
        basic = weather["weather"][0]["main"]
        description = f"Weather in Ljubljana: {basic}, {temp_c} °C"
    except:
        description = "Weather info not availibe!"


    st.write(description)

    i = 1

    top_news = get_top_headlines()
    for headline in top_news:
        st.write(f"{i}: {headline}")
        i+=1




    
news_page()
