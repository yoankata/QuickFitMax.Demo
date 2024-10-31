import streamlit as st

   # Main app
def app():

 # Sidebar
    st.header("User Settings")
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    st.session_state.max_hr = 220 - age