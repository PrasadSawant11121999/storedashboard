import streamlit as st

st.set_page_config(
    page_title="Dashboard",  # Set the page title
    page_icon="📝",  # Set the page icon (optional)
    layout="centered",  # Can be "centered" or "wide"
    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
)

def app():
    st.title('Its a Home Page')
    
app()