import streamlit as st
st.set_page_config(page_title="OIMS", page_icon="🐍")
from helper_functions import is_user_logged_in, get_token_owner_data, logout_user




# Display details of a specific order
def personal_info_page():
    st.title("Personal Details")
    data = get_token_owner_data()

    if data is None:
        st.write("Something went wrong")

    else:
        st.write(f"**Full Name**: {data['name']}")
        st.write(f"**Username**: {data['preferred_username']}")
        st.write(f"**Email**: {data['email']}")


        if st.button("Log out"):
            logout_user()
            st.switch_page("app.py")


            


personal_info_page()
