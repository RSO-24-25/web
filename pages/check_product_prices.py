import streamlit as st
st.set_page_config(page_title="OIMS", page_icon="🐍")
from statistics_helper import get_prices_graph, get_stat_prod



# Display details of a specific order
def check_product_prices_page():
    st.title("Product Prices Graph")
    st.write("Bitcon prices")
    
    id = int(get_stat_prod())

    graph = get_prices_graph(id)

    st.image(graph, caption="Prices graph", use_column_width=True)

    # st.write(f"**Product Name**: {product['name']}")



    if st.button("Back to product selection"):
        st.switch_page("pages/statistics.py")


            


check_product_prices_page()
