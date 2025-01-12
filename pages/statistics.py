# statistics.py

import streamlit as st
import pandas as pd

# Import the helper we wrote:
from statistics_helper import get_availible_products, save_stat_prod

def statistics_page():
    st.title("Choose a product")
    st.write("Choose a product to view prices' history.")

    products = get_availible_products()

    print(type(products))

    i = 0
    for product in products:
        id = product.id
        name = product.name

        i += 1

        if st.button(f"{i}: {name}"):
           
            save_stat_prod(id)
            st.switch_page("pages/check_product_prices.py")


    print(products)

    

statistics_page()
